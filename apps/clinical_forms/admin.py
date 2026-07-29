from django.contrib import admin
from .models import ClinicalFormSubmission


@admin.register(ClinicalFormSubmission)
class ClinicalFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ("form_type", "patient_name", "submitted_by_name", "computed_score", "submitted_at", "office_reviewed")
    list_filter = ("form_type", "office_reviewed")
    readonly_fields = ("submitted_at",)
