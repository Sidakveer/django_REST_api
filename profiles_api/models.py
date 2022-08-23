from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users in the system"""
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name" ]

    def get_full_name(self):
        """retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """retrieve the short name"""
        return self.name

    def __str__(self):
        """return string representation for the user"""
        return self.email
