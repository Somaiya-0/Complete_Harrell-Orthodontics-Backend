from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author_name", "source", "rating", "is_approved", "is_featured", "order")
    list_editable = ("is_approved", "is_featured", "order")
    list_filter = ("is_approved", "source")
