from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)

class UserProfile(models.Model):
    bio = models.CharField(max_length=150, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
