from rest_framework import serializers
from .models import Page, PageSection, NavCategory, DownloadableForm


class DownloadableFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadableForm
        fields = ["id", "name", "file", "order"]


class PageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSection
        fields = ["id", "page", "kind", "heading", "body", "image", "video_url", "cta_label", "cta_url", "order"]


class PageListSerializer(serializers.ModelSerializer):
    nav_category = serializers.CharField(source="nav_category.label", default=None)

    class Meta:
        model = Page
        fields = ["id", "title", "slug", "short_description", "hero_image", "nav_category", "nav_order"]


class PageDetailSerializer(serializers.ModelSerializer):
    sections = PageSectionSerializer(many=True, read_only=True)
    forms = DownloadableFormSerializer(many=True, read_only=True)
    nav_category = serializers.CharField(source="nav_category.label", default=None)

    class Meta:
        model = Page
        fields = [
            "id", "title", "slug", "short_description", "hero_image",
            "nav_category", "sections", "forms", "updated_at",
        ]


class NavCategorySerializer(serializers.ModelSerializer):
    pages = PageListSerializer(many=True, read_only=True)

    class Meta:
        model = NavCategory
        fields = ["id", "label", "order", "pages"]
