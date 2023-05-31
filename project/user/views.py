from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms.profile_form import ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from firesale.models import Item, ItemImage, Favorite, Order, Message, Bid

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "user/register.html", {'form':UserCreationForm()})

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("profile")
    return render(request, "user/profile.html", {'form': ProfileForm(instance=profile)})

def inbox(request):
    recieved_messages = Message.objects.filter(receiver=request.user)
    bids = Bid.objects.filter(user=request.user)
    return render(request, "user/inbox.html", {'messages': recieved_messages, 'bids': bids})

def my_listings(request):
    user = request.user
    available_items = Item.objects.filter(user=user, status='available')
    sold_items = Item.objects.filter(user=user, status='sold')
    item_images = ItemImage.objects.all()
    return render(request, "user/listings.html", {"available_items": available_items, 'sold_items' : sold_items, "itemimages": item_images})
        
def favorites(request):
    favorite_items = Favorite.objects.filter(member=request.user).select_related('item')
    item_images = ItemImage.objects.all()
    return render(request, "user/favorites.html", {"favorite_items": favorite_items, "itemimages": item_images})

def orders(request):
    ordered_items = Order.objects.filter(buyer=request.user).select_related('item')
    item_images = ItemImage.objects.all()
    return render(request, "user/orders.html", {"ordered_items": ordered_items, "itemimages": item_images})

def delete_offer(request, bid_id):
    bid = get_object_or_404(Bid, id=bid_id)
    item = bid.item
    if request.method == 'POST':
        # Find the administator user
        for user in User.objects.all():
            if user.username == 'administrator':
                admin = user
        message_content = f"{bid.user} cancelled their offer, so your item {item.name} is now available for bidding again."
        message = Message.objects.create(sender=admin, receiver=item.user, message=message_content)
        message.save()
        bid.delete()
        bids = Bid.objects.filter(item=item)
        # Make the item available again
        item.status = 'available'
        item.save()
        # Set past bids to pending
        for bid in bids:
            bid.status = 'pending'
            bid.save()
        return redirect('inbox')
    return render(request, 'user/delete_offer.html', {'bid': bid})
