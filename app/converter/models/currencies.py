from django.db import models


class Currencies(models.Model):
    code = models.CharField(
        max_length=3,
        primary_key=True,
        editable=False,
    )
    name = models.CharField(
        max_length=128,
    )
