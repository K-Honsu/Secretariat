from django.contrib import admin
from .models import MarriageThanksgiving, BirthNotification, ChildDedication

# Register your models here.
admin.site.register(MarriageThanksgiving)
admin.site.register(BirthNotification)
admin.site.register(ChildDedication)

