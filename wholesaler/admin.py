
from django.contrib import admin

from wholesaler.models import Wholesaler


@admin.register(Wholesaler)
class WholesalerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )
    list_filter = ("name",)
    search_fields = ("name",)
