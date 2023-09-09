from django.urls import path

from account.views import UserStatusAPIView, UserOTPAPIView

urlpatterns = [
    path('api/status/<str:phone_number>/', UserStatusAPIView.as_view(), name='user_status'),
    path('api/otp/<str:phone_number>/', UserOTPAPIView.as_view(), name='user_otp'),
]
