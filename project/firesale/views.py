from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms.member_form import MemberForm
from .forms.item_form import ItemForm
from django.contrib.auth.decorators import login_required

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
        # add filled out information to the database
        form = ItemForm(data=request.POST)
        if form.is_valid():
            item = form.save(commit=False)  # Save the item object without committing to the database yet
            item.save()  # Save the item object to generate an ID
            image_url = form.cleaned_data['image']  # Get the image URL from the form
            item_image = models.ItemImage.objects.create(item=item, img_url=image_url)  # Create the ItemImage instance and link it to the Item
            # Set the image field of the Item model to the ItemImage instance
            item.image = item_image
            # redirect the user to the members page
            return redirect("items")
    else:
        # if user has not submitted the form yet, show them a blank form
        form = ItemForm()
    return render(request, "items/create.html", {'form': form})

def item_information(request, item_id):
    item = models.Item.objects.filter(id=item_id).first()
    item_images = models.ItemImage.objects.all()
    return render(request, "items/item_information.html", {'item': item, 'itemimages': item_images})
