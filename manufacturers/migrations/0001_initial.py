# Generated by Django 4.2.2 on 2024-08-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Manufacturer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Производитель"),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                ("email", models.EmailField(max_length=254, verbose_name="Почта")),
                ("country", models.CharField(max_length=50, verbose_name="Страна")),
                ("city", models.CharField(max_length=50, verbose_name="Город")),
                ("street", models.CharField(max_length=100, verbose_name="Улица")),
                ("house", models.CharField(max_length=10, verbose_name="Дом")),
                (
                    "supplier",
                    models.CharField(max_length=100, verbose_name="Поставщик"),
                ),
                ("debt", models.FloatField(verbose_name="Задолженность")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "Производитель",
                "verbose_name_plural": "Производители",
            },
        ),
    ]
