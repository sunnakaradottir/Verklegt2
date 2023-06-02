from django.forms import ModelForm, widgets
from firesale.models import Bid
from django.core.validators import MinValueValidator

class BidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['id', 'item', 'user', 'status']
        widgets = {'bid_amount': widgets.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Enter your bid'})}
        validators=[MinValueValidator(1)]