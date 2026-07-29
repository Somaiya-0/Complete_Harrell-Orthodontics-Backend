from rest_framework import serializers
from django.utils import timezone
from .models import PatientFormSubmission, Patient


class PatientFormSubmissionSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(input_formats=["%Y-%m-%d"])

    class Meta:
        model = PatientFormSubmission
        fields = [
            "id", "first_name", "last_name", "date_of_birth", "email", "phone",
            "reason_for_visit", "is_new_patient", "referred_by",
            "has_sleep_study", "sleep_study_file", "notes", "submitted_at",
            "office_reviewed",
        ]
        read_only_fields = ["id", "submitted_at"]

    def validate_date_of_birth(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Date of birth can't be in the future.")
        return value


class PatientSerializer(serializers.ModelSerializer):
    assigned_doctor_name = serializers.CharField(source="assigned_doctor.name", read_only=True, default=None)

    class Meta:
        model = Patient
        fields = [
            "id", "first_name", "last_name", "date_of_birth", "email", "phone",
            "assigned_doctor", "assigned_doctor_name", "status", "notes",
            "source_submission", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
