from rest_framework import viewsets
from apps.accounts.permissions import IsPracticeStaff
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related("patient", "doctor").all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsPracticeStaff]
    filterset_fields = ["status", "doctor", "patient"]
