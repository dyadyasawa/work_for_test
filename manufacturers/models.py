
from django.db import models

# from wholesaler.models import Wholesaler

NULLABLE = {"blank": True, "null": True}


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Производитель')
    description = models.TextField(verbose_name='Описание')

    email = models.EmailField(verbose_name="Почта")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house = models.CharField(max_length=10, verbose_name="Дом")

    supplier = models.CharField(max_length=100, verbose_name="Поставщик")
    debt = models.FloatField(verbose_name="Задолженность", **NULLABLE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата создания')

    # wholesalers = models.ManyToManyField(Wholesaler, blank=True, null=True, related_name="wholesalers")

    def __str__(self):
        return f"Производитель: {self.name} (почта: {self.email})"

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)

    price = models.PositiveIntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата выхода на рынок')

    manufacturer = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Производитель", **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
