from django import forms
from .models import MyData

class UploadForm(forms.ModelForm):
    class Meta:
        model = MyData
        fields = ['name', 'age']