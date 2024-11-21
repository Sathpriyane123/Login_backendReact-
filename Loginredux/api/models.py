from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    """
    username = models.CharField(max_length=150, unique=True)  # Explicitly declare username
    email = models.EmailField(unique=True, null=False, blank=False)
    is_admin = models.BooleanField(default=False)  # Custom field to mark admin users
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
