from django.forms import ModelForm, widgets
from firesale.models import Bid
from django import forms

class BidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['id', 'item', 'user']
        widgets = {'bid_amount': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your bid'})}
        fields = ["bid_amount"]