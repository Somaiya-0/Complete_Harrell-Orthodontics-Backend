from django.contrib import admin
from .models import PatientFormSubmission, Patient


@admin.register(PatientFormSubmission)
class PatientFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "reason_for_visit", "submitted_at", "office_reviewed")
    list_filter = ("reason_for_visit", "office_reviewed", "is_new_patient")
    search_fields = ("first_name", "last_name", "email", "phone")
    readonly_fields = ("submitted_at",)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "assigned_doctor", "status", "created_at")
    list_filter = ("status", "assigned_doctor")
    search_fields = ("first_name", "last_name", "email", "phone")
