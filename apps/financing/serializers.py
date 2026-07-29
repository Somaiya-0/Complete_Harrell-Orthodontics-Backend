from rest_framework import serializers
from .models import FinancingOption


class FinancingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancingOption
        fields = [
            "id", "kind", "display_name", "logo", "tagline",
            "learn_more_url", "widget_script_url", "is_primary", "order",
        ]
