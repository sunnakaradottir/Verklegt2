from django.forms import ModelForm, widgets
from firesale.models import Contact
from django import forms

class ContactForm(ModelForm):
    country = forms.CharField(
        widget=forms.Select(attrs={"class": "form-control"}, choices = [
    ('', 'Select a country'),
    ('AT', 'Austria'),
    ('BE', 'Belgium'),
    ('HR', 'Croatia'),
    ('DK', 'Denmark'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('GR', 'Greece'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IE', 'Ireland'),
    ('IT', 'Italy'),
    ('NL', 'Netherlands'),
    ('NO', 'Norway'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('RU', 'Russia'),
    ('ES', 'Spain'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('TR', 'Turkey'),
    ('UA', 'Ukraine'),
    ('GB', 'United Kingdom')]))
    street_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter street name"}))
    class Meta:
        model = Contact
        exclude = ["id", "user", "address"]
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),'email': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),'phone': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}), 'house_number': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter house number'}), 'postal_code': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter postal code'}), 'city': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'})}
        fields = ['name', 'email', 'phone', 'street_name', 'house_number', 'postal_code', 'city', 'country']