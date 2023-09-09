from django.contrib.auth.backends import ModelBackend, UserModel

from account.models import OTP


class AuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            otp = OTP.validate(username, password)
            if otp:
                otp.used = True
                otp.save()
                return UserModel.objects.create(
                    phone_number=username
                )
            else:
                return
        else:
            otp_check = user.check_otp(password)
            password_check = user.check_password(password)
            if (otp_check or password_check) and self.user_can_authenticate(user):
                if otp_check:
                    otp_check.used = True
                    otp_check.save()
                return user
