from django.forms import ModelForm, widgets
from firesale.models import Item
from django import forms


class ItemForm(ModelForm):
    price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Set starting price of the item (Optional)",
            }
        ),
    )

    class Meta:
        model = Item
        exclude = ["id"]
        fields = [
            "category_id",
            "image_id",
            "member_id",
            "location_id",
            "bid_id",
            "description",
            "price",
        ]
        widgets = {
            "category": widgets.Select(attrs={"class": "form-control"}),
            "description": widgets.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Description of the item",
                }
            ),
        }
