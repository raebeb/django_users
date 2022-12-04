from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager

class User(AbstractUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculine'),
        ('F', 'Feminine'),
        ('O', 'Other'),
    )

    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    genre = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self) -> str:
        return self.username

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'