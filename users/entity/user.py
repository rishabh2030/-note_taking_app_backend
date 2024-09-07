from django.db import models
from helper.models.base_model import BaseModel
from ..services.user_manager import UserManager
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin,BaseModel):
    """
    Custom user model representing a user in the system.

    Inherits from AbstractBaseUser and PermissionsMixin for custom user authentication and permissions handling.
    Inherits BaseModel from helper for adding common fields.
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255,null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    
    def get_tokens(self):
        """Returns a tuple of JWT tokens (token, refresh_token)"""
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token), str(refresh)
    
    def __str__(self) :
        return f'{self.name}'