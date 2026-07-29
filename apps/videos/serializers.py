from rest_framework import serializers
from .models import VideoTestimonial


class VideoTestimonialSerializer(serializers.ModelSerializer):
    page_title = serializers.CharField(source="page.title", read_only=True, default=None)

    class Meta:
        model = VideoTestimonial
        fields = [
            "id", "title", "category", "video_url", "video_file", "thumbnail",
            "caption_text", "page", "page_title", "order", "is_published",
        ]
