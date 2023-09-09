from django import shortcuts
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from account.serializers import UserStatusSerializer


class UserStatusAPIView(APIView):
    def get(self, request, phone_number):
        user = shortcuts.get_object_or_404(User, phone_number=phone_number)
        return Response(
            status=status.HTTP_200_OK,
            data=UserStatusSerializer(user).data
        )
