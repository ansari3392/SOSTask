from django.conf import settings
from django.db import models
from django.utils import timezone

from services.models import Service

User = settings.AUTH_USER_MODEL


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
        related_name='requests',
    )

    class StateChoices(models.TextChoices):
        CREATED = 'created', 'ایجاد شده'
        CONFIRMED = 'confirmed', 'بررسی شده'
        FINALIZED = 'finalized', 'نهایی شده'
        CANCELED = 'canceled', 'نقص شده'

    state = models.CharField(
        'state',
        max_length=9,
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
    is_confirmed = models.BooleanField(default=False)

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

    def get_fee(self) -> int:
        fee = (self.service.price * self.user.user_type.percent) / 100
        return fee

    def get_service_request_price(self) -> int:
        if self.state == self.StateChoices.CONFIRMED:
            return self.service_price + self.fee
        return self.service.price + self.get_fee()

    def confirm_request(self) -> None:
        self.state = self.StateChoices.CONFIRMED
        self.is_confirmed = True
        self.fee = (self.service.price * self.user.user_type.percent) / 100
        self.service_price = self.service.price
        self.confirmed_at = timezone.now()
        self.save()
