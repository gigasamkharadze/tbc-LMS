from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

