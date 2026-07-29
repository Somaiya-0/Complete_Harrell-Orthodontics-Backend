from rest_framework import viewsets, parsers
from apps.accounts.permissions import IsPracticeStaffOrReadOnly
from .models import VideoTestimonial
from .serializers import VideoTestimonialSerializer


class VideoTestimonialViewSet(viewsets.ModelViewSet):
    serializer_class = VideoTestimonialSerializer
    permission_classes = [IsPracticeStaffOrReadOnly]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]
    filterset_fields = ["category", "page"]

    def get_queryset(self):
        qs = VideoTestimonial.objects.all()
        if not (self.request.user and self.request.user.is_authenticated):
            qs = qs.filter(is_published=True)
        return qs
