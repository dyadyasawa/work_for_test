
from django.db import models

from manufacturers.models import Manufacturer


class Wholesaler(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование оптовика')
    description = models.TextField(verbose_name='Описание')

    email = models.EmailField(verbose_name="Почта")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house = models.CharField(max_length=10, verbose_name="Дом")

    supplier = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Поставщик")
    debt = models.FloatField(verbose_name="Задолженность")

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата создания')

    def __str__(self):
        return f"Оптовик: {self.name}, почта: {self.email}"

    class Meta:
        verbose_name = "Оптовик"
        verbose_name_plural = "Оптовики"
