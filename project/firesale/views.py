from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms.member_form import MemberForm

# Create your views here
def index(request):
    return render(request, "base.html")


def get_members(request):
    return render(
        request, "members/index.html", {"members": models.Member.objects.all()}
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