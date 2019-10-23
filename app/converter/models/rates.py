from django.db import models
from .currencies import Currencies


class Rates(models.Model):
    base = models.ForeignKey(
        Currencies,
        on_delete=models.CASCADE,
        related_name='currency_base',
    )
    curr = models.ForeignKey(
        Currencies,
        on_delete=models.CASCADE,
        related_name='currency_curr',
    )
    value = models.FloatField()
    created = models.DateTimeField(
        auto_now_add=True,
    )
