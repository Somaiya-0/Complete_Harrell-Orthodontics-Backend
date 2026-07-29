from django.contrib import admin
from .models import Publication, Event


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "kind", "year", "order")
    list_editable = ("order",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "kind", "starts_at", "audience")
    list_filter = ("kind",)
