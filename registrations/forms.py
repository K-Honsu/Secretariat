from django.forms import ModelForm
from .models import *

class MarryForm(ModelForm):
    class Meta:
        model = MarriageThanksgiving
        fields = '__all__'
        
        
class BirthNotification(ModelForm):
    class Meta:
        model = BirthNotification
        fields = '__all__'