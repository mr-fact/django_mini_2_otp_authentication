from django.contrib import admin

from account.models import User, OTP


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    pass
