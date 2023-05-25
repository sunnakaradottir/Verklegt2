from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from .forms.member_form import MemberForm
from .forms.item_form import ItemForm
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
            item.seller_id = request.POST.get('member')
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

    item = models.Item.objects.filter(id=item_id).select_related('member').first()

    item_images = models.ItemImage.objects.all()
    return render(request, "items/item_information.html", {'item': item, 'itemimages': item_images})

@login_required
def submit_bid(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    if request.method =="POST":
        bid_amount = request.POST.get("bid-amount")
        return render(request, "items/bid.html",{"item_id":item_id})

    return redirect("item_information", item_id=item_id)
