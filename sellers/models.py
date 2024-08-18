
from django.db import models

from creditors.models import Creditor
from wholesaler.models import Wholesaler

NULLABLE = {"blank": True, "null": True}


class Seller(models.Model):
    name = models.CharField(max_length=100, verbose_name='Продавец')
    description = models.TextField(verbose_name='Описание')

    email = models.EmailField(verbose_name="Почта")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house = models.CharField(max_length=10, verbose_name="Дом")

    wholesaler = models.ManyToManyField(Wholesaler, blank=True, related_name="wholesaler")
    creditors = models.ManyToManyField(Creditor, verbose_name="Кредиторы", blank=True, related_name="creditors_for_seller")

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата создания')

    def __str__(self):
        return f"Продавец: {self.name} (почта: {self.email})"

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"
        ordering = ("city",)
