from django.contrib.auth.models import AbstractUser
from django.db import models

from account.models import UserType


class CustomUser(AbstractUser):
    user_type = models.ForeignKey(
        UserType,
        on_delete=models.CASCADE,
        related_name='users',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
