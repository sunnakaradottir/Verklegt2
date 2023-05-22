from django.forms import ModelForm, widgets
from firesale.models import Member


class MemberForm(ModelForm):
    class Meta:
        model = Member
        exclude = ["id"]
        fields = ["image_id", "name", "phone", "birthday", "bio"]
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
