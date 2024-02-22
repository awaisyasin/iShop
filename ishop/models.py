from django.db import models

from accounts.models import CustomUser

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000)
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='shop')
    created_at = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=11, help_text='Enter the phone number without spaces or special characters, e.g., 03012345678')
    website = models.URLField(null=True, blank=True, help_text='Enter the URL starting with http:// or https://')