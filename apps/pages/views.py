from rest_framework import viewsets, parsers
from apps.accounts.permissions import IsPracticeStaffOrReadOnly
from .models import Page, NavCategory, PageSection
from .serializers import (
    PageListSerializer, PageDetailSerializer, NavCategorySerializer, PageSectionSerializer,
)


class NavigationView(viewsets.ReadOnlyModelViewSet):
    queryset = NavCategory.objects.prefetch_related("pages").all()
    serializer_class = NavCategorySerializer


class PageViewSet(viewsets.ModelViewSet):
    """Public read of published pages; staff dashboard does full CRUD
    (title/slug/hero image/etc.) via the 'Manage content' screen."""
    lookup_field = "slug"
    permission_classes = [IsPracticeStaffOrReadOnly]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]

    def get_queryset(self):
        qs = Page.objects.select_related("nav_category").prefetch_related("sections", "forms")
        if not (self.request.user and self.request.user.is_authenticated):
            qs = qs.filter(is_published=True)
        return qs

    def get_serializer_class(self):
        if self.action == "retrieve" or self.request.method not in ("GET",):
            return PageDetailSerializer
        return PageListSerializer


class PageSectionViewSet(viewsets.ModelViewSet):
    """Staff-only: add/edit/reorder the content blocks within a page."""
    queryset = PageSection.objects.all()
    serializer_class = PageSectionSerializer
    permission_classes = [IsPracticeStaffOrReadOnly]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]
    filterset_fields = ["page"]
