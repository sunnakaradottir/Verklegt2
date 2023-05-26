from django.forms import ModelForm, widgets
from firesale.models import Item
from django import forms

class ItemForm(ModelForm):
    price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Set starting price of the item (Optional)"})
    )
    category = forms.ChoiceField(
        choices=[('', 'Select a category'),('category1', 'Children'), ('category2', 'Clothing'), ('category3', 'Electronics'), ('category4', 'Home'), ('category5', 'Entertainment'), ('category6', 'Sports & Health'), ('category7', 'Toys & Hobbies'), ('category8', 'Vehicle'), ('category9', 'Other')],
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "Category"})
    )
    image = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Item image URL"})
    )
    class Meta:
        model = Item
        exclude = ["id", "category", "location", "image", "creation_date"]
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Item name", "required": "true"}),
            "condition": widgets.Select(attrs={"class": "form-control", "placeholder": "Condition"}, choices=[('', 'Select condition'),('brand_new', 'Brand new'), ('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')]),
            "description": widgets.Textarea(attrs={"class": "form-control", "placeholder": "Description of the item"}),
        }
        fields = ["name", "category", "condition", "price", "description"]  # Specify the desired order of fields
