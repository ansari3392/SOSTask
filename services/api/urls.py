from django.urls import path

from services.api.views.confirm_request import ConfirmRequestAPIView
from services.api.views.service_request import RequestServiceAPIView

app_name = 'api'

urlpatterns = [
    path('request-service/', RequestServiceAPIView.as_view(), name='request_service'),
    path('confirm-request/', ConfirmRequestAPIView.as_view(), name="confirm_request"),

]
