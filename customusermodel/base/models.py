from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    # def __str__(self):
    #     return self.username  # or any other field you want to represent the user by
