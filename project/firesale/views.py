from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


# Create your views here
def index(request):
    return render(request, "base.html")


def get_members(request):
    return render(
        request, "members/index.html", {"members": models.Member.objects.all()}
    )