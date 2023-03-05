from django.forms import ModelForm
from .models import *

class MarryForm(ModelForm):
    class Meta:
        model = MarriageThanksgiving
        fields = ['family_name', 'band_of_husband', 'band_of_wife', 'father_unit_name', 'mother_unit_name']
        
        
class BirthNotifications(ModelForm):
    class Meta:
        model = BirthNotification
        fields = '__all__'
        
class ChildDedications(ModelForm):
    class Meta:
        model = ChildDedication
        fields = '__all__'