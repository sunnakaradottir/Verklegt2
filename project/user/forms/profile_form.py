from django.forms import ModelForm, widgets
from user.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),'favorite_candy': widgets.Select(attrs={'class': 'form-control'}), 'profile_image': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a URL for your profile image'})}