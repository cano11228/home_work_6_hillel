from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    bio = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=7, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
