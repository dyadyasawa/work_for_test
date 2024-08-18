
from django.contrib import admin

from creditors.models import Creditor


@admin.register(Creditor)
class CreditorAdmin(admin.ModelAdmin):
    list_display = (
        "creditor",
        "debtor",
        "amount",
    )
    list_filter = ("creditor",)
    search_fields = ("creditor",)
