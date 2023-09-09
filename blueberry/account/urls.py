from django.urls import path

from account.views import UserStatusAPIView

urlpatterns = [
    path('api/status/<str:phone_number>/', UserStatusAPIView.as_view(), name='user_status'),
]
