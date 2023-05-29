from django.forms import ModelForm, widgets
from firesale.models import Contact
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ["id", "user"]
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),'email': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),'phone': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),'address': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}), 'postal_code': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter postal code'}), 'city': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}), 'country': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country'})}
        fields = ['name', 'email', 'phone', 'address', 'postal_code', 'city', 'country']