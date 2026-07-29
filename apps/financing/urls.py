from rest_framework.routers import DefaultRouter
from .views import FinancingOptionViewSet

router = DefaultRouter()
router.register("options", FinancingOptionViewSet, basename="financing-option")

urlpatterns = router.urls
