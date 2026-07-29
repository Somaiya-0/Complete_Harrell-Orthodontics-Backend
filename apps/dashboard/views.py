from datetime import timedelta
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.accounts.permissions import IsPracticeStaff
from apps.team.models import TeamMember
from apps.patients.models import Patient, PatientFormSubmission
from apps.appointments.models import Appointment
from apps.referrals.models import ReferralSubmission


class DashboardStatsView(APIView):
    """Overview cards + a couple of simple report series for the staff
    dashboard home screen."""
    permission_classes = [IsPracticeStaff]

    def get(self, request):
        now = timezone.now()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        week_ago = now - timedelta(days=7)

        appointment_status_breakdown = {
            choice_value: Appointment.objects.filter(status=choice_value).count()
            for choice_value, _ in Appointment.Status.choices
        }

        data = {
            "total_doctors": TeamMember.objects.filter(is_doctor=True).count(),
            "total_patients": Patient.objects.count(),
            "active_patients": Patient.objects.filter(status=Patient.Status.ACTIVE).count(),
            "appointments_today": Appointment.objects.filter(
                scheduled_at__gte=today_start, scheduled_at__lt=today_end
            ).count(),
            "new_intake_forms_week": PatientFormSubmission.objects.filter(submitted_at__gte=week_ago).count(),
            "unreviewed_intake_forms": PatientFormSubmission.objects.filter(office_reviewed=False).count(),
            "pending_referrals": ReferralSubmission.objects.filter(office_reviewed=False).count(),
            "appointment_status_breakdown": appointment_status_breakdown,
        }
        return Response(data)
