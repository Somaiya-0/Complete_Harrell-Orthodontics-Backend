from rest_framework.routers import DefaultRouter
from .views import PublicationViewSet, EventViewSet

router = DefaultRouter()
router.register("items", PublicationViewSet, basename="publication")
router.register("events", EventViewSet, basename="event")

urlpatterns = router.urls
