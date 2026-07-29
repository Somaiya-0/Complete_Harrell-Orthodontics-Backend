from django.contrib import admin
from .models import ExternalProvider, ReferralSubmission


@admin.register(ExternalProvider)
class ExternalProviderAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "location", "order")
    list_editable = ("order",)


@admin.register(ReferralSubmission)
class ReferralSubmissionAdmin(admin.ModelAdmin):
    list_display = ("patient_name", "referral_type", "submitted_by", "submitted_at", "office_reviewed")
    list_filter = ("referral_type", "office_reviewed")
