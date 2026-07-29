from rest_framework import generics, permissions, throttling, viewsets
from django.core.mail import send_mail
from django.conf import settings
from apps.accounts.permissions import IsPracticeStaff
from .models import PatientFormSubmission, Patient
from .serializers import PatientFormSubmissionSerializer, PatientSerializer


class PatientIntakeThrottle(throttling.AnonRateThrottle):
    rate = "10/hour"


class PatientFormSubmissionCreateView(generics.CreateAPIView):
    """Public endpoint the 'New Patient Online Form' posts to."""
    queryset = PatientFormSubmission.objects.all()
    serializer_class = PatientFormSubmissionSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [PatientIntakeThrottle]

    def perform_create(self, serializer):
        submission = serializer.save()
        self._notify_office(submission)

    def _notify_office(self, submission):
        try:
            send_mail(
                subject=f"New patient form: {submission.first_name} {submission.last_name}",
                message=(
                    f"Reason for visit: {submission.get_reason_for_visit_display()}\n"
                    f"DOB: {submission.date_of_birth:%m/%d/%Y}\n"
                    f"Phone: {submission.phone}\nEmail: {submission.email}\n"
                    f"Notes: {submission.notes}"
                ),
                from_email=settings.SITE_CONTACT_EMAIL,
                recipient_list=[settings.PATIENT_FORM_NOTIFY_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass


class PatientFormSubmissionViewSet(viewsets.ModelViewSet):
    """Staff dashboard: view/triage online-form submissions."""
    queryset = PatientFormSubmission.objects.all()
    serializer_class = PatientFormSubmissionSerializer
    permission_classes = [IsPracticeStaff]
    http_method_names = ["get", "patch", "delete", "head", "options"]


class PatientViewSet(viewsets.ModelViewSet):
    """Staff dashboard: full patient-of-record management."""
    queryset = Patient.objects.select_related("assigned_doctor").all()
    serializer_class = PatientSerializer
    permission_classes = [IsPracticeStaff]
    filterset_fields = ["status", "assigned_doctor"]
    search_fields = ["first_name", "last_name", "email", "phone"]
