from django.forms import ModelForm, widgets
from firesale.models import Message
from django import forms

class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['id', 'item', 'user', 'status']
        widgets = {'message': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Message'})}