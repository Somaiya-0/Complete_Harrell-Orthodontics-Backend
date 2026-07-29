from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "author_name", "source", "rating", "body", "review_date", "is_featured", "is_approved", "submitted_at"]
        read_only_fields = ["id", "is_approved", "submitted_at", "is_featured", "source", "review_date"]


class ReviewStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ["id", "submitted_at"]
