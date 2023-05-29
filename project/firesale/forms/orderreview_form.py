from django.forms import ModelForm, widgets
from firesale import models
from django import forms

class OrderReviewForm(ModelForm):
    class Meta:
        model = models.Order
        exclude = ["id", "item", "buyer", "seller", "creation_time", "contact", "payment"]