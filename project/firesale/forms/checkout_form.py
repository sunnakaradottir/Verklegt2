from django.forms import ModelForm
from django import forms
from firesale import models

class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        exclude = ["id", "user"]
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter message'})}

class PaymentForm(ModelForm):
    class Meta:
        model = models.Payment
        exclude = ["id", "bid", "user"]
        widgets = {'cardholder_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name of cardholder as seen on card'}),'card_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card number'}),'expiration_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Expiration date'}),'cvc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVC'})}
