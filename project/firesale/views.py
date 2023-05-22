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
        print(1)
    else:
        form = MemberForm()
    return render(request, "members/create.html", {'form': form})