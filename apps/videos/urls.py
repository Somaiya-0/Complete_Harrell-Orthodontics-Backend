from rest_framework.routers import DefaultRouter
from .views import VideoTestimonialViewSet

router = DefaultRouter()
router.register("", VideoTestimonialViewSet, basename="video")

urlpatterns = router.urls
