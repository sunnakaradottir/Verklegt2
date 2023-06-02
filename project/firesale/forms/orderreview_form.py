from django.forms import ModelForm
from firesale import models

class OrderReviewForm(ModelForm):
    class Meta:
        model = models.Order
        exclude = ["id", "item", "buyer", "seller", "creation_time", "contact", "payment"]