from django.forms import ModelForm, widgets
from firesale.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        exclude = ['order', 'from_user', 'to_user', 'creation_time', 'from_member', 'to_member']
        widgets = {
            'rating': widgets.Select(attrs={"class": "form-control"}, choices=[
                (-1, 'Select a rating'),
                (0, '0'),
                (1, '1'),
                (2, '2'),
                (3, '3'),
                (4, '4'),
                (5, '5'),
            ]), 'comment': widgets.TextInput(attrs={"class": "form-control", 'placeholder': 'Leave a comment explaining your review'})
        }
