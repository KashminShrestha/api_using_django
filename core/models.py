from django.db import models
from django.contrib.auth.models import AbstractUser
from core.managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    otp = models.PositiveIntegerField(null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()
