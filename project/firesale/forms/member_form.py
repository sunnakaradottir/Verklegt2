from django.forms import ModelForm, widgets
from firesale.models import Member
from django import forms


class MemberForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Image URL"}))
    class Meta:
        model = Member
        exclude = ["id", "image_id"]
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "form-control", "placeholder": "Full name"}
            ),
            "phone": widgets.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone number"}
            ),
            "birthday": widgets.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "bio": widgets.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "A little bit about yourself...",
                }
            ),
        }
