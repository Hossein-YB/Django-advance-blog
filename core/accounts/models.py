from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db.models import EmailField
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """manager for Custom User Model for create user"""

    def create_user(self, email, password, **extra_fields):
        """check user object email and password """
        if not email:
            raise ValueError(_("email most be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """for crate a super user"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("super user is_staff most be True is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("super user is_superuser most be True is_superuser=True"))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
        Custom User model for our app
    """
    email = models.EmailField(max_length=300, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> EmailField:
        return self.email

