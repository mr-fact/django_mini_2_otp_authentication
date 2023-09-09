from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not phone_number:
            raise ValueError("The phone number must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        if password:
            user.set_password(password)
            user.save()
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(phone_number, password, **extra_fields)


phone_validator = RegexValidator(
    regex=r'09\d{9}',
    message='phone number must be entered in the (09---------) format '
)


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, validators=[phone_validator, ])
    username = None

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def check_otp(self, otp):
        return otp == '1111'
