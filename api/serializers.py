from rest_framework import serializers
from registrations.models import ChildDedication, BirthNotification, MarriageThanksgiving

class ChildSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChildDedication
        fields = '__all__'
        
        
class BirthNotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = BirthNotification
        fields = '__all__'
        
        
class MarriageThanksGivingSerializers(serializers.ModelSerializer):
    class Meta:
        model = MarriageThanksgiving
        fields = '__all__'