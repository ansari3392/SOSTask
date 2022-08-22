from django.db import models
from django.db.models import Q


class UserType(models.Model):
    name = models.CharField(max_length=150, unique=True)
    percent = models.FloatField(default=0)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                condition=Q(is_default=True),
                fields=['is_default'],
                name="unique_default_user_type"
            )
        ]
