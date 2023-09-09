from django.contrib import admin

from account.models import User, OTP


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'password', ]


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'otp', 'user', 'created_at', ]
