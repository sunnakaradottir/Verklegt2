from django.forms import ModelForm, widgets
from firesale.models import Item, Category
from django import forms

class ItemForm(ModelForm):
    price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Set starting price of the item (Optional)"})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select a category',
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "Category"})
    )
    image = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Item image URL"})
    )
    class Meta:
        model = Item
        exclude = ["id", "creation_date"]
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Item name", "required": "true"}),
            "condition": widgets.Select(attrs={"class": "form-control", "placeholder": "Condition"}, choices=[('', 'Select condition'),('Brand new', 'Brand new'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')]),
            "description": widgets.Textarea(attrs={"class": "form-control", "placeholder": "Description of the item"}),
            "item_location": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Set the location of the item"}),
        }
        labels = {
            "item_location": "Location",
        }
        fields = ["name", "category", "condition", "price", "description", "item_location"]

