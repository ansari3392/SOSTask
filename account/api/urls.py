from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.api.views.change_password import ChangePasswordView
from account.api.views.register import RegisterView

app_name = 'api'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('access/', TokenObtainPairView.as_view(), name='access'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),

]
