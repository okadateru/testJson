from django import forms
from django.forms import ModelForm
from .models import NewAPIResponse


class APIResponseForm(ModelForm):

    class Meta:
        model = NewAPIResponse

        fields = ['success', 'image_path']

