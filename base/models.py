from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=350, null=True, blank=True)
    message = models.TextField(max_length=1000, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
