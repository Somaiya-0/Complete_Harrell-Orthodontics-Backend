from django.contrib import admin
from .models import FinancingOption


@admin.register(FinancingOption)
class FinancingOptionAdmin(admin.ModelAdmin):
    list_display = ("display_name", "kind", "is_primary", "order", "is_active")
    list_editable = ("order", "is_primary", "is_active")
