from django.forms import ModelForm, widgets
from django.core.exceptions import ValidationError
from firesale import models
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone

class PaymentForm(ModelForm):
    card_number = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Card number, 16 digits'}),
        validators=[MinLengthValidator(16), MaxLengthValidator(16)]
    )
    cvc = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CVC'}),
        validators=[MinLengthValidator(3), MaxLengthValidator(3)]
    )

    expiration_date = forms.DateField(
        input_formats=['%m/%y'],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Expiration date (MM/YY)'}),
    )

    def clean_expiration_date(self):
        expiration_date = self.cleaned_data['expiration_date']
        if expiration_date < timezone.now().date():
            raise ValidationError("Expiration date is in the past.")
        return expiration_date

    class Meta:
        model = models.Payment
        exclude = ["id", "bid", "user"]
        widgets = {
            'cardholder_name': widgets.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Enter name of cardholder as seen on card (max 100 char)'})
        }
        fields = ['cardholder_name', 'card_number', 'expiration_date', 'cvc']
