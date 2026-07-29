from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ExternalProviderViewSet,
    ReferralSubmissionCreateListView,
    ReferralSubmissionDetailView,
)


router = DefaultRouter()

router.register(
    "providers",
    ExternalProviderViewSet,
    basename="external-provider"
)


urlpatterns = [
    # GET all referrals + POST new referral
    path(
        "submissions/",
        ReferralSubmissionCreateListView.as_view(),
        name="referral-submissions"
    ),

    # GET one referral + PATCH update + DELETE referral
    path(
        "submissions/<int:pk>/",
        ReferralSubmissionDetailView.as_view(),
        name="referral-detail"
    ),

    # Provider directory
    path(
        "",
        include(router.urls)
    ),
]