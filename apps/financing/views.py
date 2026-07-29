from rest_framework import viewsets, parsers
from apps.accounts.permissions import IsPracticeStaffOrReadOnly
from .models import FinancingOption
from .serializers import FinancingOptionSerializer


class FinancingOptionViewSet(viewsets.ModelViewSet):
    serializer_class = FinancingOptionSerializer
    permission_classes = [IsPracticeStaffOrReadOnly]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]

    def get_queryset(self):
        qs = FinancingOption.objects.all()
        if not (self.request.user and self.request.user.is_authenticated):
            qs = qs.filter(is_active=True)
        return qs
