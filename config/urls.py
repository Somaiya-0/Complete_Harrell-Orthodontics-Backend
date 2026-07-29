from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.accounts.urls")),
    path("api/pages/", include("apps.pages.urls")),
    path("api/patients/", include("apps.patients.urls")),
    path("api/financing/", include("apps.financing.urls")),
    path("api/videos/", include("apps.videos.urls")),
    path("api/team/", include("apps.team.urls")),
    path("api/publications/", include("apps.publications.urls")),
    path("api/referrals/", include("apps.referrals.urls")),
    path("api/reviews/", include("apps.reviews.urls")),
    path("api/appointments/", include("apps.appointments.urls")),
    path("api/dashboard/", include("apps.dashboard.urls")),
    path("api/clinical-forms/", include("apps.clinical_forms.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
