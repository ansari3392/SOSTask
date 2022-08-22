from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.api.views.change_password import ChangePasswordAPIView
from account.api.views.register import RegisterAPIView

app_name = 'api'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('access/', TokenObtainPairView.as_view(), name='access'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('change_password/<int:pk>/', ChangePasswordAPIView.as_view(), name='change_password'),
]
