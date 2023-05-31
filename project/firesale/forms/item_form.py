from django.forms import ModelForm, widgets
from firesale.models import Item, Category
from django import forms

class ItemForm(ModelForm):
    price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "min": 0, "placeholder": "Set starting price of the item (Optional)"})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select a category',
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "Category"})
    )
    image_urls = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter image URLs, one URL per line up to four (Optional)", "rows": 4}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['image_urls'].widget.attrs['size'] = '4'
    
    class Meta:
        model = Item
        exclude = ["id", "creation_date", "status", "user"]
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Item name", "required": "true"}),
            "condition": widgets.Select(attrs={"class": "form-control", "placeholder": "Condition"}, choices=[('', 'Select condition'),('Brand new', 'Brand new'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')]),
            "description": widgets.Textarea(attrs={"class": "form-control", "placeholder": "Description of the item"}),
            "item_location": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Set the location of the item"}),
        }
        fields = ["name", "category", "condition", "price", "description", "item_location", "image_urls"]
        labels = {
            "item_location": "Location",
        }

