from rest_framework import viewsets, parsers
from apps.accounts.permissions import IsPracticeStaffOrReadOnly
from .models import TeamMember
from .serializers import TeamMemberSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    """Public GET (published only); staff dashboard does full CRUD +
    photo upload (multipart)."""
    serializer_class = TeamMemberSerializer
    permission_classes = [IsPracticeStaffOrReadOnly]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]

    def get_queryset(self):
        qs = TeamMember.objects.all()
        if not (self.request.user and self.request.user.is_authenticated):
            qs = qs.filter(is_published=True)
        return qs
