from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from . import models
from .forms.bid_form import BidForm
from .forms.contact_form import ContactForm
from .forms.payment_form import PaymentForm
from .forms.orderreview_form import OrderReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import Item, ItemImage
from user.models import Profile


# Create your views here

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = []
        itemimages = ItemImage.objects.all()

        for item_found in Item.objects.filter(name__icontains=search_filter):
            for itemimage in itemimages:
                if itemimage.item == item_found:
                    items.append({'id': item_found.id, 'name': item_found.name, 'image': itemimage.img_url,
                                  'category': item_found.category.name,
                                  'condition': item_found.condition,
                                  'item_location': item_found.item_location,
                                  'price': item_found.price})




        return JsonResponse({'data': items})
    items = Item.objects.all()
    itemimages = ItemImage.objects.all()

    return render(request, "items/index.html",
                  {"items": items,
                   "itemimages": itemimages,
                   'include_item_information': True, })


def get_members(request):
    return render(
        request, "members/index.html",
        {"members": models.Member.objects.all(), "memberimages": models.MemberImage.objects.all()}
    )


def create_member(request):
    if request.method == "POST":
        # add filled out information to the database
        form = forms.MemberForm(data=request.POST)
        if form.is_valid():
            # create a new member object and save it to the database
            member = form.save()
            # create a new image object and save it to the database
            member_image = models.MemberImage(request.POST['image'], member_id=member)
            member_image.save()
            # redirect the user to the members page
            return redirect("members")
    return render(request, "members/create.html", {'form': forms.MemberForm()})


@login_required
def create_item(request):
    if request.method == "POST":
        form = forms.ItemForm(data=request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            category = models.Category.objects.filter(name=form.cleaned_data['category'])
            if category:
                item.category = category.first()
            item.save()

            image_url = form.cleaned_data['image']
            item_image = ItemImage.objects.create(item=item, img_url=image_url)
            item.image = item_image
            return redirect("index")
    return render(request, "items/create_item.html", {'form': forms.ItemForm()})


def delete_item(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return redirect('item_information', item_id=item_id)


def item_information(request, item_id):
    item = models.Item.objects.filter(id=item_id).first()
    item_images = models.ItemImage.objects.all()
    highest_bid = models.Bid.objects.filter(item=item).aggregate(Max('bid_amount'))['bid_amount__max']

    similar_items = models.Item.objects.filter(category=item.category).exclude(id=item.id)[:3]

    return render(request, "items/item_information.html",
                  {'item': item, 'itemimages': item_images, "highest_bid": highest_bid, 'similar_items': similar_items})


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
    item_images = models.ItemImage.objects.all()
    bid = get_object_or_404(models.Bid, id=bid_id)
    # Bid is accepted
    bid.status = 'accepted'
    bid.save()
    # Create a message from the sender to the reciever
    sender = request.user
    receiver = bid.user
    message_content = f"Your bid of ${bid.bid_amount} on {item.name} has been accepted!"
    message = models.Message.objects.create(sender=sender, receiver=receiver, message=message_content, bid=bid)
    return render(request, "items/item_bids.html", {'item': item, 'itemimages': item_images, 'bids': bids})

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
    # Delete bid / Only show pending bids?
    render(request, "items/item_bids.html", {'item': item, 'itemimages': item_images, 'bids': bids})

@login_required()
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
    all_items = Item.objects.all()
    item_images = models.ItemImage.objects.all()
    sort_option = request.GET.get('sort_option', 'name')  # Default to sorting by name if no option is selected

    if sort_option == 'name_asc':
        all_items = all_items.order_by('name')
    elif sort_option == 'name_desc':
        all_items = all_items.order_by('-name')
    elif sort_option == 'price_asc':
        all_items = all_items.order_by('price')
    elif sort_option == 'price_desc':
        all_items = all_items.order_by('-price')
    # Add more sorting options if needed

    # Pass the sorted items queryset and sort_option to the template context
    context = {
        "items": all_items,
        "itemimages": item_images,
        'sort_option': sort_option,
        # Other context variables
    }
    return render(request, "items/index.html", context)

def contact_info(request, bid_id):
    bid = get_object_or_404(models.Bid, id=bid_id)
    if request.method == 'POST':
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
            return redirect('payment_info', bid_id=bid_id, contact_id=contact.id)
        else:
            print("Form errors:", form.errors)
    return render(request, "items/contact_info.html", {'form': ContactForm(), 'bid': bid, 'contact': contact})

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
    return render(request, "items/payment_info.html", {'form': PaymentForm(), 'bid': bid})

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
            order.seller = bid.user
            order.item = bid.item
            order.contact = contact
            order.payment = payment
            order.save()
            return redirect('index') #change so the user is redirected to my orders
    return render(request, "items/order_review.html", {'bid': bid, 'contact': contact, 'payment': payment, 'form': OrderReviewForm()})