from django import shortcuts
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User, OTP
from account.serializers import UserStatusSerializer


class UserStatusAPIView(APIView):
    def get(self, request, phone_number):
        user = shortcuts.get_object_or_404(User, phone_number=phone_number)
        return Response(
            status=status.HTTP_200_OK,
            data=UserStatusSerializer(user).data
        )


class UserOTPAPIView(APIView):
    def get(self, request, phone_number):
        try:
            otp = OTP.get_or_create_otp(phone_number)
        except ValidationError as err:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'details': err})
        return Response(status=status.HTTP_200_OK, data={'details': 'otp sent', 'otp': otp.otp})
