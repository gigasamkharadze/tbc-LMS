from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    
    username = models.CharField(max_length=150, unique=True, verbose_name=_('Username'))
    email = models.EmailField(unique=True, verbose_name=_('Email address'))
    password = models.CharField(max_length=128, verbose_name=_('Password'))

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
