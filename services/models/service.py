from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=250,)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
