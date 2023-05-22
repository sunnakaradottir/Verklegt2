from django.forms import ModelForm, widgets
from firesale.models import Item
from django import forms


class ItemForm(ModelForm):
    price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Set starting price of the item (Optional)"})
    )

    class Meta:
        model = Item
        exclude = ["id"]
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Item name"}),
            "category": widgets.Select(attrs={"class": "form-control", "placeholder": "Category"}),
            "condition": widgets.Select(attrs={"class": "form-control", "placeholder": "Condition"}),
            "price": widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Item price"}),
            "description": widgets.Textarea(attrs={"class": "form-control", "placeholder": "Description of the item"}),
        }
