from rest_framework import generics, viewsets, permissions, throttling
from django.core.mail import send_mail
from django.conf import settings
from apps.accounts.permissions import IsPracticeStaff
from .models import ClinicalFormSubmission
from .serializers import ClinicalFormSubmissionSerializer


class ClinicalFormThrottle(throttling.AnonRateThrottle):
    rate = "20/hour"


class ClinicalFormSubmitView(generics.CreateAPIView):
    """Public endpoint every digitized form (Epworth, STOP-BANG, TMJ Pain
    Scale, C-GASP, CPAP Intolerance, Referral) posts to."""
    queryset = ClinicalFormSubmission.objects.all()
    serializer_class = ClinicalFormSubmissionSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [ClinicalFormThrottle]

    def perform_create(self, serializer):
        submission = serializer.save()
        try:
            send_mail(
                subject=f"New {submission.get_form_type_display()} submission: {submission.patient_name or 'unnamed'}",
                message=(
                    f"Form: {submission.get_form_type_display()}\n"
                    f"Patient: {submission.patient_name}\n"
                    f"Referring/submitted by: {submission.submitted_by_name}\n"
                    f"Score: {submission.computed_score}\n\n"
                    f"Answers: {submission.answers}"
                ),
                from_email=settings.SITE_CONTACT_EMAIL,
                recipient_list=[settings.PATIENT_FORM_NOTIFY_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass


class ClinicalFormSubmissionViewSet(viewsets.ModelViewSet):
    """Staff dashboard: review submitted clinical forms."""
    queryset = ClinicalFormSubmission.objects.all()
    serializer_class = ClinicalFormSubmissionSerializer
    permission_classes = [IsPracticeStaff]
    filterset_fields = ["form_type", "office_reviewed"]
