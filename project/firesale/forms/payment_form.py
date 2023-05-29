from django.forms import ModelForm, widgets
from firesale import models
from django import forms

class PaymentForm(ModelForm):
    card_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Card number, 16 digits'}))
    cvc = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CVC'}))
    class Meta:
        model = models.Payment
        exclude = ["id", "bid", "user"]
        widgets = {'cardholder_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name of cardholder as seen on card (max 100 char)'}), 'expiration_date': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Expiration date (YYYY-MM-DD)'})}
        fields = ['cardholder_name', 'card_number', 'expiration_date', 'cvc']
    