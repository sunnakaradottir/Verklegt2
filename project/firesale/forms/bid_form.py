from django.forms import ModelForm, widgets
from firesale.models import Bid
from django import forms

class BidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['id', 'item', 'user', 'status']
        widgets = {'bid_amount': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your bid (Numerical input between -2147483648 and 2147483647)'})}