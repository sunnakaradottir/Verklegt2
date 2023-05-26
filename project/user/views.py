from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms.profile_form import ProfileForm
from .models import Profile

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
    return render(request, "user/inbox.html")