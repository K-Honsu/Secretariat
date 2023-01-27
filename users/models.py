from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    second_name = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False, primary_key=True)
    
    
    def __str__(self):
        return self.user
    
    

