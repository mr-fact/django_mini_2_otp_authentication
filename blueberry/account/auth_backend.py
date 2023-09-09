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
            if OTP.validate(username, password):
                return UserModel.objects.create(
                    phone_number=username
                )
        else:
            if (user.check_password(password) or user.check_otp(password)) and self.user_can_authenticate(user):
                return user
        return None
