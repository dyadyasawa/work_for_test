# Generated by Django 4.2.2 on 2024-08-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("creditors", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="creditor",
            name="debtor",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Должник"
            ),
        ),
    ]
