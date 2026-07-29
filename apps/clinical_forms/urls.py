from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClinicalFormSubmitView, ClinicalFormSubmissionViewSet

router = DefaultRouter()
router.register("submissions", ClinicalFormSubmissionViewSet, basename="clinical-form-submission")

urlpatterns = [
    path("submit/", ClinicalFormSubmitView.as_view(), name="clinical-form-submit"),
    path("", include(router.urls)),
]
