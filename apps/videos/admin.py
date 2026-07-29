from django.contrib import admin
from .models import VideoTestimonial


@admin.register(VideoTestimonial)
class VideoTestimonialAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order", "is_published")
    list_editable = ("order", "is_published")
