from django.forms import ModelForm, widgets
from firesale.models import Contact
from django import forms

class ContactForm(ModelForm):
    country = forms.CharField(
        widget=forms.Select(attrs={"class": "form-control"}, choices = [
    ('', 'Select a country'),
    ('Austria', 'Austria'),
    ('Belgium', 'Belgium'),
    ('Croatia', 'Croatia'),
    ('Denmark', 'Denmark'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('Germany', 'Germany'),
    ('Greece', 'Greece'),
    ('Hungary', 'Hungary'),
    ('Iceland', 'Iceland'),
    ('Ireland', 'Ireland'),
    ('Italy', 'Italy'),
    ('Netherlands', 'Netherlands'),
    ('Norway', 'Norway'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Russia', 'Russia'),
    ('Spain', 'Spain'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Turkey', 'Turkey'),
    ('Ukraine', 'Ukraine'),
    ('United Kingdom', 'United Kingdom')]))
    street_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter street name"}))
    class Meta:
        model = Contact
        exclude = ["id", "user", "address"]
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),'email': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),'phone': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}), 'house_number': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter house number'}), 'postal_code': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter postal code'}), 'city': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'})}
        fields = ['name', 'email', 'phone', 'street_name', 'house_number', 'postal_code', 'city', 'country']