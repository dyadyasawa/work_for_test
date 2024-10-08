# Generated by Django 4.2.2 on 2024-08-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wholesaler", "0002_remove_wholesaler_supplier"),
        ("manufacturers", "0007_manufacturer_wholesalers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manufacturer",
            name="wholesalers",
            field=models.ManyToManyField(
                blank=True, related_name="wholesalers", to="wholesaler.wholesaler"
            ),
        ),
    ]
