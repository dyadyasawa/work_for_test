
from django.db import models

from creditors.models import Creditor
from manufacturers.models import Manufacturer


class Wholesaler(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование оптовика')
    description = models.TextField(verbose_name='Описание')

    email = models.EmailField(verbose_name="Почта")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house = models.CharField(max_length=10, verbose_name="Дом")

    manufacturer = models.ManyToManyField(Manufacturer, blank=True, related_name="manufacturer")
    creditors = models.ManyToManyField(Creditor, verbose_name="Кредиторы", blank=True, related_name="creditors_for_wholesaler")

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата создания')

    def __str__(self):
        return f"Оптовик: {self.name}, почта: {self.email}"

    class Meta:
        verbose_name = "Оптовик"
        verbose_name_plural = "Оптовики"
        ordering = ("city",)
