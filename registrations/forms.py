from django.forms import ModelForm
from .models import *

class MarryForm(ModelForm):
    class Meta:
        model = MarriageThanksgiving
        fields = '__all__'