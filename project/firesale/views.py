from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from .forms.member_form import MemberForm
from .forms.item_form import ItemForm
from .forms.bid_form import BidForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Item, ItemImage

# Create your views here
def index(request):
    return render(request, "items/index.html", {"items": models.Item.objects.all(), "itemimages": models.ItemImage.objects.all(), 'include_item_information': True,})

def get_members(request):
    return render(
        request, "members/index.html", {"members": models.Member.objects.all(), "memberimages": models.MemberImage.objects.all()}
    )

def create_member(request):
    if request.method == "POST":
        # add filled out information to the database
        form = MemberForm(data=request.POST)
        if form.is_valid():
            # create a new member object and save it to the database
            member = form.save()
            # create a new image object and save it to the database
            member_image = models.MemberImage(request.POST['image'], member_id=member)
            member_image.save()
            # redirect the user to the members page
            return redirect("members")
    else:
        # if user has not submitted the form yet, show them a blank form
        form = MemberForm()
    return render(request, "members/create.html", {'form': form})

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

            image_url = form.cleaned_data['image']
            item_image = ItemImage.objects.create(item=item, img_url=image_url)
            item.image = item_image
            return redirect("index")
    else:
        form = ItemForm()
    return render(request, "items/create_item.html", {'form': form})

def delete_item(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return redirect('item_information', item_id=item_id) 

def item_information(request, item_id):
    item = models.Item.objects.filter(id=item_id).first()
    item_images = models.ItemImage.objects.all()
    return render(request, "items/item_information.html", {'item': item, 'itemimages': item_images})

@login_required
def create_bid(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    if request.method =="POST":
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
    return render(request, "items/item_bids.html", {'item': item, 'itemimages': item_images, 'bids': bids})

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
    message_content = "Your bid has been accepted!"
    message = models.Message.objects.create(sender=sender, receiver=receiver, message=message_content)
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
    message_content = "Your bid has been rejected."
    message = models.Message.objects.create(sender=sender, receiver=receiver, message=message_content)
    # Delete bid / Only show pending bids?
    return render(request, "items/item_bids.html", {'item': item, 'bid': bid})

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
    return render(request, "items/index.html", {"items": items, "itemimages": item_images, "categories": categories, "selected_category": selected_category})
