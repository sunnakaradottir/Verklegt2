from django.forms import ModelForm, widgets
from firesale import models
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        exclude = ["id", "user"]
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}), 'postal_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter postal code'}), 'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}), 'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country'})}
        fields = ['name', 'email', 'phone', 'address', 'postal_code', 'city', 'country']