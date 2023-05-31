from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import JsonResponse
from . import models
from .forms.bid_form import BidForm
from .forms.contact_form import ContactForm
from .forms.payment_form import PaymentForm
from .forms.item_form import ItemForm
from .forms.orderreview_form import OrderReviewForm
from .forms.review_form import ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from user.models import Profile


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = []
        for item_found in models.Item.objects.filter(name__icontains=search_filter):
            for itemimage in models.ItemImage.objects.filter(item=item_found):
                items.append({'id': item_found.id, 'name': item_found.name, 'image': itemimage.img_url,
                            'category': item_found.category.name,
                            'condition': item_found.condition,
                            'item_location': item_found.item_location,
                            'price': item_found.price})
                return JsonResponse({'data': items})
    items = models.Item.objects.all()
    itemimages = models.ItemImage.objects.all()
    return render(request, "items/index.html", {"items": items, "itemimages": itemimages, 'include_item_information': True})

@login_required
def create_item(request):
    if request.method == "POST":
        form = ItemForm(data=request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            category = models.Category.objects.filter(name=form.cleaned_data['category'])
            if category:
                item.category = category.first()
            item.save()

            selected_image_urls = form.cleaned_data['image_urls'].split('\n')
            for image_url in selected_image_urls:
                item_image, _ = models.ItemImage.objects.get_or_create(img_url=image_url, item=item)
                item.image_urls.add(item_image)
            return redirect("index")
    return render(request, "items/create_item.html", {'form': ItemForm()})

def delete_item(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return redirect('item_information', item_id=item_id)

def item_information(request, item_id):
    item = models.Item.objects.filter(id=item_id).first()
    item_images = models.ItemImage.objects.filter(item=item)
    highest_bid = models.Bid.objects.filter(item=item).aggregate(Max('bid_amount'))['bid_amount__max']

    similar_items = models.Item.objects.filter(category=item.category).exclude(id=item.id)[:3]
    is_favorite = False
    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'favorites' in request.POST:
                favorite = models.Favorite.objects.create(member=request.user, item=item)
                favorite.save()
            elif 'remove_favorite' in request.POST:
                models.Favorite.objects.filter(member=request.user, item=item).delete()
            return redirect('item_information', item_id=item_id)
        else:
            return redirect('login')
    if request.user.is_authenticated:
        is_favorite = models.Favorite.objects.filter(member=request.user, item=item).exists()
    return render(request, "items/item_information.html", {
        'item': item,
        'itemimages': item_images,
        'highest_bid': highest_bid,
        'similar_items': similar_items,
        'is_favorite': is_favorite})

@login_required
def create_bid(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    if request.method == "POST":
        form = BidForm(data=request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.item = item
            bid.user = request.user
            bid.save()
            return redirect("item_information", item_id=item_id)
        else:
            print("Form errors:", form.errors)
    return render(request, "items/bid.html", {'form': BidForm(), 'item': item})

@login_required
def view_bids(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    item_images = models.ItemImage.objects.all()
    bids = models.Bid.objects.filter(item=item_id)
    user_profiles = Profile.objects.filter(user__in=[bid.user for bid in bids])
    user_profiles_map = {profile.user_id: profile for profile in user_profiles}
    return render(request, "items/item_bids.html", {'item': item, 'itemimages': item_images, 'bids': bids, 'user_profiles': user_profiles_map})

def accept_bid(request, item_id, bid_id):
    item = get_object_or_404(models.Item, id=item_id)
    bids = models.Bid.objects.filter(item=item_id)
    bid = get_object_or_404(models.Bid, id=bid_id)
    # Bid is accepted
    bid.status = 'accepted'
    bid.save()
    # Reject all other bids
    for otherbid in bids:
        if otherbid != bid:
            otherbid.status = 'rejected'
            otherbid.save()
    # Create a message from the sender to the reciever
    sender = request.user
    receiver = bid.user
    message_content = f"Your bid of ${bid.bid_amount} on {item.name} has been accepted!"
    message = models.Message.objects.create(sender=sender, receiver=receiver, message=message_content, bid=bid)
    # Mark the item as sold so it cannot be bid on again
    item.status = 'sold'
    item.save()
    return redirect('index')

def reject_bid(request, item_id, bid_id):
    item = get_object_or_404(models.Item, id=item_id)
    bids = models.Bid.objects.filter(item=item_id)
    item_images = models.ItemImage.objects.all()
    bid = get_object_or_404(models.Bid, id=bid_id)
    # Bid is rejected
    bid.status = 'rejected'
    bid.save()
    # Create a message from the sender to the reciever
    sender = request.user
    receiver = bid.user
    message_content = f"Your bid of ${bid.bid_amount} on {item.name} has been rejected."
    message = models.Message.objects.create(sender=sender, receiver=receiver, message=message_content, bid=bid)
    #TODO: Only show pending bids to the seller
    render(request, "items/item_bids.html", {'item': item, 'itemimages': item_images, 'bids': bids})

@login_required
def profile(request):
    member = models.Member.objects.get(user=request.user)
    memberimages = models.MemberImage.objects.filter(member=member)
    return render(request, 'user/profile.html', {'profile': profile, 'memberimages': memberimages})

def filtered_categories(request, category_id):
    selected_category = int(category_id)
    items = models.Item.objects.all()
    item_images = models.ItemImage.objects.all()
    if selected_category:
        items = items.filter(category_id=selected_category)
    categories = models.Category.objects.all()

    is_category_empty = not items.exists()

    context = {
        "items": items,
        "itemimages": item_images,
        "categories": categories,
        "selected_category": selected_category,
        "is_category_empty": is_category_empty
    }

    return render(request, "items/index.html", context)

def sort_items(request):
    all_items = models.Item.objects.all()
    item_images = models.ItemImage.objects.all()
    sort_option = request.GET.get('sort_option', 'name')

    if sort_option == 'name_asc':
        all_items = all_items.order_by('name')
    elif sort_option == 'name_desc':
        all_items = all_items.order_by('-name')
    elif sort_option == 'price_asc':
        all_items = all_items.order_by('price')
    elif sort_option == 'price_desc':
        all_items = all_items.order_by('-price')

    context = {
        "items": all_items,
        "itemimages": item_images,
        'sort_option': sort_option,
    }
    return render(request, "items/index.html", context)

def contact_info(request, bid_id):
    bid = get_object_or_404(models.Bid, id=bid_id)
    if request.method == 'POST':
        if 'back' in request.POST:
            return redirect('inbox')
        form = ContactForm(data=request.POST)
        if form.is_valid(): # if the form is valid then we save the it
            contact = form.save(commit=False)
            contact.user = request.user
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.phone = form.cleaned_data['phone']
            contact.address = form.cleaned_data['address']
            contact.postal_code = form.cleaned_data['postal_code']
            contact.city = form.cleaned_data['city']
            contact.country = form.cleaned_data['country']
            contact.save()
            return redirect('payment_info', bid_id=bid.id, contact_id=contact.id)
        else:
            print("Form errors:", form.errors)
    return render(request, "items/contact_info.html", {'form': ContactForm(), 'bid': bid})

def payment_info(request, bid_id, contact_id):
    bid = get_object_or_404(models.Bid, id=bid_id)
    contact = get_object_or_404(models.Contact, id=contact_id)
    if request.method == 'POST':
        if 'back' in request.POST:
            contact.delete()
            return redirect('contact_info', bid_id=bid_id)
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.bid = bid
            payment.cardholder_name = form.cleaned_data['cardholder_name']
            payment.card_number = form.cleaned_data['card_number']
            payment.expiration_date = form.cleaned_data['expiration_date']
            payment.cvc = form.cleaned_data['cvc']
            payment.save()
            return redirect('order_review', bid_id=bid_id, contact_id=contact_id, payment_id=payment.id)
        else:
            print("Form errors:", form.errors)
    return render(request, "items/payment_info.html", {'form': PaymentForm(), 'bid': bid, 'contact': contact})

def order_review(request, bid_id, contact_id, payment_id):
    bid = get_object_or_404(models.Bid, id=bid_id)
    contact = get_object_or_404(models.Contact, id=contact_id)
    payment = get_object_or_404(models.Payment, id=payment_id)
    if request.method == 'POST':
        if 'back' in request.POST:
            payment.delete()
            return redirect('payment_info', bid_id=bid_id, contact_id=contact_id)
        form = OrderReviewForm(data=request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.buyer = contact.user
            order.seller = bid.item.user
            order.item = bid.item
            order.contact = contact
            order.payment = payment
            order.save()
            return redirect('rating_seller', bid_id=bid_id, contact_id=contact_id, payment_id=payment_id, order_id=order.id)
    return render(request, "items/order_review.html", {'bid': bid, 'contact': contact, 'payment': payment, 'form': OrderReviewForm()})

def about_page(request):
    return render(request, 'pages/about.html')

def terms_page(request):
    return render(request, 'pages/terms.html')

def faq_page(request):
    return render(request, 'pages/faq.html')

def contact_page(request):
    return render(request, 'pages/contact.html')

def calc_avg_rating(user):
    '''Calculates the average rating of a user based on the reviews they have received'''
    reviews = models.Review.objects.filter(to_user=user)
    ratings_list = [review.rating for review in reviews if review.rating is not None]
    if len(ratings_list) > 0:
        average_rating = sum(ratings_list) / len(ratings_list)
    else:
        average_rating = 0.0
    return average_rating

def rating_seller(request, bid_id, contact_id, payment_id, order_id):
    bid = get_object_or_404(models.Bid, id=bid_id)
    contact = get_object_or_404(models.Contact, id=contact_id)
    payment = get_object_or_404(models.Payment, id=payment_id)
    order = get_object_or_404(models.Order, id=order_id)

    if request.method == 'POST':
        ordered_items = models.Order.objects.filter(buyer=request.user).select_related('item')
        item_images = models.ItemImage.objects.all()
        if 'norating' in request.POST:
            return render(request, 'user/orders.html', {"ordered_items": ordered_items, "itemimages": item_images})
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.order = order
            review.to_user = bid.item.user
            review.from_user = request.user
            review.comment = form.cleaned_data['comment']
            review.rating = form.cleaned_data['rating']
            review.save()
            average_rating = calc_avg_rating(bid.item.user)
            bid.item.user.profile.average_rating = average_rating
            bid.item.user.profile.save()
            return render(request, 'user/orders.html', {"ordered_items": ordered_items, "itemimages": item_images})
        else:
            print("Form errors:", form.errors)
    return render(request, 'items/rating_seller.html', {'form': ReviewForm(), 'order': order, 'bid': bid, 'contact': contact, 'payment': payment})
