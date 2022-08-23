from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.api.views.change_password import ChangePasswordAPIView
from account.api.views.login import GetAccessTokenAPIView
from account.api.views.register import RegisterAPIView
from account.api.views.reset_password import ResetPasswordRequestAPIView, PasswordTokenCheckAPIView, \
    SetNewPasswordAPIView
from account.api.views.verify_email import VerifyEmailAPIView

app_name = 'api'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('email-verify/', VerifyEmailAPIView.as_view(), name="email_verify"),
    path('access/', GetAccessTokenAPIView.as_view(), name='access'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('change-password/<int:pk>/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('reset-password-request/', ResetPasswordRequestAPIView.as_view(), name='reset_password_request'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')

]
