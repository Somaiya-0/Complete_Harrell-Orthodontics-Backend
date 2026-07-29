from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PatientFormSubmissionCreateView, PatientFormSubmissionViewSet, PatientViewSet

router = DefaultRouter()
router.register("submissions", PatientFormSubmissionViewSet, basename="patient-submission")
router.register("records", PatientViewSet, basename="patient-record")

urlpatterns = [
    path("submit/", PatientFormSubmissionCreateView.as_view(), name="patient-form-submit"),
    path("", include(router.urls)),
]
