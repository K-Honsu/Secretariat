from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Contact
from django.forms import ModelForm


class ContactField(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'