from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.db.models import F
from django.utils import timezone

from services.models import Service

User = get_user_model()


class RequestService(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='services',
        db_index=True,
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='request',
    )

    class StateChoices(models.TextChoices):
        CREATED = 'created', 'ایجاد شده'
        CONFIRMED = 'confirmed', 'بررسی شده'
        FINALIZED = 'finalized', 'نهایی شده'
        CANCELED = 'canceled', 'نقص شده'

    state = models.CharField(
        'state',
        max_length=10,
        default=StateChoices.CREATED,
        choices=StateChoices.choices,
        db_index=True,
    )
    user_extra_description = models.TextField(
        null=True,
        blank=True
    )

    staff_extra_description = models.TextField(
        null=True,
        blank=True
    )
    photo = models.ImageField(
        upload_to="images",
        validators=[
            getattr(
                validators,
                'FileExtensionValidator')(
                allowed_extensions=[
                    'jpg',
                    'png',
                ])],
    )
    service_price = models.PositiveBigIntegerField(
        null=True,
        blank=True,
        help_text='این فیلد در لحظه ی تایید شدن درخواست،'
                  ' به صورت اتوماتیک ذخیره میشود تا در صورت تغییر قیمت سرویس،'
                  ' درخواست های ثبت شده تغییر قیمت نداشته باشند.'
    )
    fee = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='این فیلد در لحظه ی تایید شدن درخواست،'
                  ' به صورت اتوماتیک ذخیره میشود تا در صورت تغییر درصد کارمزد و یا تغییر نوع عضویت کاربر،'
                  ' درخواست های ثبت شده تغییر قیمت نداشته باشند.'
    )

    is_verified = models.BooleanField(default=False)

    confirmed_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.service.name

    class Meta:
        verbose_name = 'Request Service'
        verbose_name_plural = 'Request Services'

    @staticmethod
    def get_fee():
        fee = F('service__price') * F('user__user_type__percent')
        return fee

    def get_service_request_price(self):
        total_price = (F('service__price') + self.get_fee())
        return total_price

    def confirm_request(self):
        self.state = self.StateChoices.CONFIRMED

        fee = self.user.user_type.percent
        self.fee = fee

        price = self.service.price
        self.service_price = price

        self.confirmed_at = timezone.now()

        self.save()
