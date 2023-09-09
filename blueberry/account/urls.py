from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from account.views import UserStatusAPIView, UserOTPAPIView

urlpatterns = [
    path('api/status/<str:phone_number>/', UserStatusAPIView.as_view(), name='user_status'),
    path('api/otp/<str:phone_number>/', UserOTPAPIView.as_view(), name='user_otp'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
