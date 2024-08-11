
from django.db import models

# from manufacturers.models import Manufacturer
# from wholesaler.models import Wholesaler
#
#
# class Debtor(models.Model):
#     name_creditor = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Наименование кредитора')
#     name_debtor = models.ForeignKey(Wholesaler, on_delete=models.CASCADE, verbose_name='Наименование должника')
#     amount_of_debt = models.FloatField(verbose_name="Сумма долга", blank=True, null=True)
#
#     def __str__(self):
#         return f"Должник: {self.name_debtor}, (Кредитор: {self.name_creditor}, сумма долга: {self.amount_of_debt})"
#
#     class Meta:
#         verbose_name = "Должник"
#         verbose_name_plural = "Должники"
