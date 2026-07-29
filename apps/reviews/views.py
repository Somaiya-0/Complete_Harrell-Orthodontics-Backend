from rest_framework import viewsets, generics, permissions, throttling
from django.core.mail import send_mail
from django.conf import settings
from apps.accounts.permissions import IsPracticeStaff
from .models import Review
from .serializers import ReviewSerializer, ReviewStaffSerializer


class ReviewSubmitThrottle(throttling.AnonRateThrottle):
    rate = "5/hour"


class ReviewListPublicView(generics.ListAPIView):
    """Only approved reviews are shown publicly -- fixes spelling errors
    and screens content before anything goes live, per the client's
    'admin approval before publishing' requirement."""
    queryset = Review.objects.filter(is_approved=True)
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]


class ReviewSubmitView(generics.CreateAPIView):
    """Public 'Leave a review' form -- lands unapproved and emails the
    office for moderation."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [ReviewSubmitThrottle]

    def perform_create(self, serializer):
        review = serializer.save(source=Review.Source.WEBSITE, is_approved=False)
        try:
            send_mail(
                subject=f"New review submitted by {review.author_name}",
                message=f"Rating: {review.rating}/5\n\n{review.body}\n\nApprove in the staff dashboard or Django Admin before it appears on the site.",
                from_email=settings.SITE_CONTACT_EMAIL,
                recipient_list=[settings.PATIENT_FORM_NOTIFY_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass


class ReviewStaffViewSet(viewsets.ModelViewSet):
    """Staff dashboard: approve/edit (fix spelling)/feature/delete reviews."""
    queryset = Review.objects.all()
    serializer_class = ReviewStaffSerializer
    permission_classes = [IsPracticeStaff]
    filterset_fields = ["is_approved", "is_featured", "source"]
