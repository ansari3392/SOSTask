from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('access/', TokenObtainPairView.as_view(), name='access'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]
