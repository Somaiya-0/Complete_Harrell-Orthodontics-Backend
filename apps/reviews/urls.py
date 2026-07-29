from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewListPublicView, ReviewSubmitView, ReviewStaffViewSet

router = DefaultRouter()
router.register("manage", ReviewStaffViewSet, basename="review-manage")

urlpatterns = [
    path("", ReviewListPublicView.as_view(), name="review-list"),
    path("submit/", ReviewSubmitView.as_view(), name="review-submit"),
    path("", include(router.urls)),
]
