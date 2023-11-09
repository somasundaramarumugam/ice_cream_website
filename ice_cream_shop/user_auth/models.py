from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     
    mobile_number = models.BigIntegerField(blank=True, null=True) 
    def __str__(self): 
        return self.user.username
