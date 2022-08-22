from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.api.views.change_password import ChangePasswordAPIView
from account.api.views.register import RegisterAPIView
from account.api.views.reset_password import ResetPasswordRequestAPIView, PasswordTokenCheckAPIView

app_name = 'api'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('access/', TokenObtainPairView.as_view(), name='access'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('change_password/<int:pk>/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('reset_password/', ResetPasswordRequestAPIView.as_view(), name='reset_password_request'),
    path('password_reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name='password_reset_confirm'),

]
