from django.urls import path, include
app_name = 'services'

urlpatterns = [
    path('services/', include('services.api.urls'))
]
