from django.db import models


class UserType(models.Model):
    name = models.CharField(max_length=150, unique=True)
    percent = models.FloatField(default=0)

    def __str__(self):
        return self.name
