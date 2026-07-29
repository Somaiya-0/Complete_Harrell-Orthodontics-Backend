from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import ExternalProvider, ReferralSubmission
from .serializers import (
    ExternalProviderSerializer,
    ReferralSubmissionSerializer,
)


class ExternalProviderViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provider directory.
    Visible only to authenticated users inside the referral portal.
    """

    queryset = ExternalProvider.objects.all()
    serializer_class = ExternalProviderSerializer
    permission_classes = [IsAuthenticated]


class ReferralSubmissionCreateListView(generics.ListCreateAPIView):
    """
    GET:
        - Staff/Admin -> see all referrals
        - Referring provider -> see only their own referrals

    POST:
        - Referring providers can submit referrals
    """

    serializer_class = ReferralSubmissionSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user

        # Office staff/admin can see all referrals
        if (
            user.is_superuser
            or user.is_staff
            or user.role == user.Role.STAFF
        ):
            return ReferralSubmission.objects.all()

        # Referring providers only see their own submissions
        return ReferralSubmission.objects.filter(
            submitted_by=user
        )


class ReferralSubmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET:
        View single referral

    PATCH:
        Update referral status (office_reviewed)

    DELETE:
        Delete referral (staff/admin)
    """

    serializer_class = ReferralSubmissionSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user

        # Staff/admin can update/delete any referral
        if (
            user.is_superuser
            or user.is_staff
            or user.role == user.Role.STAFF
        ):
            return ReferralSubmission.objects.all()

        # Referring providers can only access their own referrals
        return ReferralSubmission.objects.filter(
            submitted_by=user
        )