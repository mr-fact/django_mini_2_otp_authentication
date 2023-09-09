from datetime import datetime, timedelta
from random import randint

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


phone_validator = RegexValidator(
    regex=r'09\d{9}',
    message='phone number must be entered in the (09---------) format '
)


class OTP(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='OTPs', null=True, blank=True, default=None
    )
    phone_number = models.CharField(max_length=15, validators=[phone_validator, ])
    created_at = models.DateTimeField(default=datetime.now)
    otp = models.CharField(max_length=15)
    used = models.BooleanField(default=False)

    @classmethod
    def validate(cls, phone_number, otp_code):
        try:
            return cls.objects.get(
                phone_number=phone_number,
                otp=otp_code,
                created_at__gte=datetime.now()-timedelta(minutes=5),
                used=False
            )
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_or_create_otp(cls, phone_number):
        try:
            return cls.objects.get(
                phone_number=phone_number,
                created_at__gte=datetime.now() - timedelta(minutes=5)
            )
        except cls.DoesNotExist:
            otp = cls(
                phone_number=phone_number,
                otp=f'{randint(100000, 999999)}'
            )
            otp.full_clean()
            otp.save()
            return otp


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not phone_number:
            raise ValueError("The phone number must be set")
        user = User(phone_number=phone_number, **extra_fields)
        user.full_clean()
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


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, validators=[phone_validator, ])
    username = None

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def check_otp(self, otp_code):
        return OTP.validate(self.phone_number, otp_code)
