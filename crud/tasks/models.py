from os import name
from django.db import models
from django.db.models.fields import CharField


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    data = models.DateTimeField(null=False)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name