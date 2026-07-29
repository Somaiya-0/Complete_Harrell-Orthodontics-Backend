from rest_framework import serializers
from .models import ClinicalFormSubmission


class ClinicalFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalFormSubmission
        fields = [
            "id", "form_type", "patient_name", "submitted_by_name",
            "answers", "computed_score", "submitted_at", "office_reviewed",
        ]
        read_only_fields = ["id", "submitted_at"]
