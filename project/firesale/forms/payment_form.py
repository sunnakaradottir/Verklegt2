from django.forms import ModelForm, widgets
from firesale import models
from django import forms

class PaymentForm(ModelForm):
    class Meta:
        model = models.Payment
        exclude = ["id", "bid", "user"]
        widgets = {'cardholder_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name of cardholder as seen on card'}),'card_number': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card number'}),'expiration_date': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Expiration date'}),'cvc': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVC'})}
        fields = ['cardholder_name', 'card_number', 'expiration_date', 'cvc']