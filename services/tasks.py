from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.utils import timezone

from .models.request_service import RequestService


@shared_task
def cancel_confirmed_requests():
    expire: int = settings.REQUEST_EXPIRE_TIME
    request_service = RequestService.objects.filter(
        state=RequestService.StateChoices.CONFIRMED,
        confirmed_at__lte=timezone.now() - timedelta(seconds=expire)
    )
    result = request_service.update(state=RequestService.StateChoices.CANCELED)
    return result

