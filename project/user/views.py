from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms.profile_form import ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from firesale.models import Bid
from firesale.models import Message
from firesale.models import Item, ItemImage, Favorite, Order

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
    return render(request, "user/profile.html",{'form': ProfileForm(instance=profile)})

def inbox(request):
    recieved_messages = Message.objects.filter(receiver=request.user)
    bids = Bid.objects.filter(user=request.user)
    return render(request, "user/inbox.html", {'messages': recieved_messages, 'bids': bids})

def my_listings(request):
    user = request.user
    items = Item.objects.filter(user=user)
    item_images = ItemImage.objects.all()
    return render(request, "user/listings.html", {"items": items, "itemimages": item_images})

#Þetta er kannski ehv skrítið þarf að skoða betur
def update_average_rating(self):
    ratings = self.user.seller_ratings.values_list('rating', flat=True)
    if ratings:
        self.average_rating = sum(ratings) / len(ratings)
        self.save()
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
    if request.method == 'POST':
        # Logic to delete the offer
        bid.delete()
        return redirect('inbox')
    return render(request, 'user/delete_offer.html', {'bid': bid})
