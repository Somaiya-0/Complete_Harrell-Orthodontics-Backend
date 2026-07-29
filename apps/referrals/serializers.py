from rest_framework import serializers
from .models import ExternalProvider, ReferralSubmission


class ExternalProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalProvider
        fields = ["id", "name", "specialty", "location", "email"]


# class ReferralSubmissionSerializer(serializers.ModelSerializer):
    submitted_by_name = serializers.CharField(source="submitted_by.get_full_name", read_only=True)

    class Meta:
        model = ReferralSubmission
        fields = [
            "id",
            "referral_type",
            "patient_name",
            "patient_dob",
            "notes",
            "attachment",
            "submitted_at",
            "office_reviewed",
            "submitted_by_name",
        ]
        read_only_fields = ["id", "submitted_at", "submitted_by_name"]

    def create(self, validated_data):
        # office_reviewed should never be settable on create, even by staff
        validated_data.pop("office_reviewed", None)
        validated_data["submitted_by"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context["request"]
        if not (request.user.is_staff or request.user.role == request.user.Role.STAFF):
            validated_data.pop("office_reviewed", None)
        return super().update(instance, validated_data)

class ReferralSubmissionSerializer(serializers.ModelSerializer):

    submitted_by_name = serializers.SerializerMethodField()

    class Meta:
        model = ReferralSubmission
        fields = [
            "id",
            "referral_type",
            "patient_name",
            "patient_dob",
            "notes",
            "attachment",
            "submitted_at",
            "submitted_by_name",
            "office_reviewed",
        ]

    def get_submitted_by_name(self, obj):
        user = obj.submitted_by
        return f"{user.first_name} {user.last_name}".strip() or user.username

    def create(self, validated_data):
        validated_data["submitted_by"] = self.context["request"].user
        return super().create(validated_data)