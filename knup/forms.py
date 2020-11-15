from django import forms
from .models import File
from django.forms import ClearableFileInput

class UploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = {'storedname'}
        widgets = {
            'storedname': ClearableFileInput(attrs={'multiple': True}),
        }