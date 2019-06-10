from django import forms
from django.forms import ModelForm
from .models import APIResponse


class APIresponseForm(ModelForm):

    class Meta:
        model = APIResponse

        fields = ['data']
