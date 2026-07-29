from rest_framework import serializers
from .models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = [
            "id", "name", "role_title", "credentials", "specialty", "bio",
            "education", "years_experience", "photo", "is_doctor",
            "accepting_new_patients", "order", "is_published", "updated_at",
        ]
        read_only_fields = ["id", "updated_at"]
