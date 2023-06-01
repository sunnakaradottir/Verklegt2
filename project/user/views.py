from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms.profile_form import ProfileForm
from .forms.notification_settings_form import NotificationSettingsForm
from .models import Profile, NotificationSettings
from django.contrib.auth.models import User
from firesale.models import Item, ItemImage, Favorite, Order, Message, Bid, Review
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else: 
        form = UserCreationForm()
    return render(request, "user/register.html", {'form':form})

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your information has been updated successfully.')
            return redirect("profile")
    return render(request, "user/profile.html", {'form': ProfileForm(instance=profile)})

def inbox(request):
    recieved_messages = Message.objects.filter(receiver=request.user)
    bids = Bid.objects.filter(user=request.user)
    return render(request, "user/inbox.html", {'messages': recieved_messages, 'bids': bids})

def my_listings(request):
    user = request.user
    items = Item.objects.filter(user=user)
    available_items = Item.objects.filter(user=user, status='available')
    sold_items = Item.objects.filter(user=user, status='sold')
    item_images = ItemImage.objects.all()
    return render(request, "user/listings.html", { "items": items,"available_items": available_items, 'sold_items' : sold_items, "itemimages": item_images})
        
def favorites(request):
    favorite_items = Favorite.objects.filter(member=request.user).select_related('item')
    item_images = ItemImage.objects.all()
    return render(request, "user/favorites.html", {"favorite_items": favorite_items, "itemimages": item_images})

def orders(request):
    ordered_items = Order.objects.filter(buyer=request.user).select_related('item')
    item_images = ItemImage.objects.all()
    return render(request, "user/orders.html", {"ordered_items": ordered_items, "itemimages": item_images})

def my_reviews(request):
    user = request.user
    reviews = Review.objects.filter(to_user=user)
    return render(request, "user/reviews.html", {"reviews": reviews})

def send_email(email_address, message_content):
    subject = "FireSale Notification!"
    message = message_content
    from_email = "cpianalyzer@outlook.com"
    recipient_list = [email_address]

    try:
        send_mail(subject, message, from_email, recipient_list)
        return True
    except Exception as e:
        print(str(e))
        return False
    
def delete_offer(request, bid_id):
    bid = get_object_or_404(Bid, id=bid_id)
    item = bid.item
    if request.method == 'POST':
        # Find the administator user
        for user in User.objects.all():
            if user.username == 'administrator':
                admin = user
        # If the user has email notifications on
        message_content = f"{bid.user} cancelled their offer, so your item {item.name} is now available for bidding again."
        if item.user.notificationsettings.email_notifications:
            send_email(item.user.notificationsettings.email_address, message_content)
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
            message_content2 = f"Your offer for of {bid.bid_amount} on {item.name} has been set to pending, since the accepted bidder cancelled the offer."
            if bid.user.notificationsettings.email_notifications:
                send_email(bid.user.notificationsettings.email_address, message_content2)
            receiver = bid.user
            message2 = Message.objects.create(sender=admin, receiver=receiver, message=message_content2)
            message2.save()
        return redirect('inbox')
    return render(request, 'user/delete_offer.html', {'bid': bid})

def notification_settings(request):
    notification_settings = NotificationSettings.objects.filter(user=request.user).first()
    if request.method=='POST':
        form = NotificationSettingsForm(request.POST, instance=notification_settings)
        if form.is_valid():
            notification_settings = form.save(commit=False)
            notification_settings.user = request.user
            notification_settings.save()
            items = Item.objects.all()
            itemimages = ItemImage.objects.all()
            return render(request, "items/index.html", {"items": items, "itemimages": itemimages})
    return render(request, 'user/notification_settings.html', {'form':NotificationSettingsForm(instance=notification_settings)})