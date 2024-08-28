
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Creditor(models.Model):
    creditor = models.CharField(max_length=100, verbose_name="Кредитор")
    debtor = models.CharField(max_length=100, verbose_name="Должник", **NULLABLE)
    amount = models.FloatField(verbose_name="Сумма долга", **NULLABLE)

    def __str__(self):
        return f"Кредитор: {self.creditor}  Должник: {self.debtor} (сумма долга: {self.amount})"

    class Meta:
        verbose_name = "Кредитор"
        verbose_name_plural = "Кредиторы"
