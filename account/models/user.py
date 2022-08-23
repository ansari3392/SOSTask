from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db import models
from django.http import HttpRequest
from django.urls import reverse
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode

from account.models import UserType
from utils.token import create_temp_token


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    user_type = models.ForeignKey(
        UserType,
        on_delete=models.CASCADE,
        related_name='users',
    )
    is_active = models.BooleanField(
        'active',
        default=False,
        help_text=("Designates whether this user should be treated as active. "
                   "Unselect this instead of deleting accounts."),
    )
    email = models.EmailField(
        unique=True,
    )
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        if not self.pk and not self.user_type_id:
            default_user_type = UserType.objects.filter(is_default=True).first()
            if default_user_type:
                self.user_type = default_user_type
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    def send_activation_link(self, request: HttpRequest) -> None:
        payload = {'user_id': self.id}
        token: str = create_temp_token(payload)
        current_site = get_current_site(request).domain
        relativeLink = reverse('account:api:email_verify')
        abs_url = 'http://' + current_site + relativeLink + "?token=" + str(token)
        message = 'Hi ' + self.first_name + \
                  ' Use the link below to verify your email \n' + abs_url
        send_mail(
            subject='Verify your email',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.email]
        )

    def send_reset_password_link(self, request: HttpRequest) -> None:
        uidb64 = urlsafe_base64_encode(smart_bytes(self.id))
        token = PasswordResetTokenGenerator().make_token(self)
        current_site = get_current_site(
            request=request).domain
        message = 'Hello, \n Use link below to reset your password  \n' + \
                  'http://' + current_site + reverse(
            'account:api:password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        send_mail(
            subject='Reset your password',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.email]
        )

    def activate(self):
        self.is_active = True
        self.save()
