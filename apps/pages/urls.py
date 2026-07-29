from rest_framework.routers import DefaultRouter
from .views import PageViewSet, NavigationView, PageSectionViewSet

router = DefaultRouter()
router.register("nav", NavigationView, basename="nav")
router.register("sections", PageSectionViewSet, basename="page-section")
router.register("", PageViewSet, basename="page")

urlpatterns = router.urls
