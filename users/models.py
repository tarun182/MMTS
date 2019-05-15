from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    account_id     =  models.AutoField(auto_created=True, primary_key=True)
    email          =  models.EmailField(unique=True)
    full_name      =  models.CharField(max_length=20)
    mobile_no      =  models.IntegerField(blank=False)
    date_joined    =  models.DateTimeField(default=timezone.now)
    balance        =  models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #date_of_birth  =  models.DateTimeField(blank=False, default=timezone.now)

    location = (
        ('B', 'Banglore'),
        ('P', 'Pune'),
        ('H', 'Hyderabad'),
        ('D', 'Delhi'),
        ('G', 'Gurugaon'),
    )
    loc = models.CharField(max_length=1, choices=location)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
