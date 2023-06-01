from django import forms
from user.models import NotificationSettings
from django.forms import ModelForm, widgets

class NotificationSettingsForm(ModelForm):
    class Meta:
        model = NotificationSettings
        exclude = ['user']
        fields = ['email_notifications', 'email_address']
        widgets = {'email_notifications': widgets.CheckboxInput(attrs={'class': 'form-check-input'}), 'email_address': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})}