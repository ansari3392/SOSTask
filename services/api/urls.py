from django.urls import path

from services.api.views.get_user_requests import GetUserRequestsAPIView
from services.api.views.service_request import RequestServiceDetailAPIView, \
    RequestServiceUpdateAPIView, RequestServiceCreateAPIView, ConfirmRequestServiceAPIView

app_name = 'api'

urlpatterns = [
    path('request-service/', RequestServiceCreateAPIView.as_view(), name='request_service'),
    path('confirm-request/', ConfirmRequestServiceAPIView.as_view(), name="confirm_request"),
    path('request-detail/<int:pk>/', RequestServiceDetailAPIView.as_view(), name="request_detail"),
    path('edit-request/<int:pk>/', RequestServiceUpdateAPIView.as_view(), name="edit_request"),
    path('edit-request/<int:pk>/', RequestServiceUpdateAPIView.as_view(), name="edit_request"),
    path('get-user-request/', GetUserRequestsAPIView.as_view(), name="get_user_request"),
]
