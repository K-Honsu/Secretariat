from django.db import models

# Create your models here.
class MarriageThanksgiving(models.Model):
    family_name = models.CharField(max_length=1000)
    band_of_husband = models.CharField(max_length=350)
    band_of_wife = models.CharField(max_length=350)
    date_of_marriage = models.DateTimeField(auto_now_add=True)
