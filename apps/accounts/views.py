from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RoleTokenObtainPairSerializer, MeSerializer


class RoleTokenObtainPairView(TokenObtainPairView):
    """Login endpoint for the referring-provider portal."""
    serializer_class = RoleTokenObtainPairSerializer


class MeView(RetrieveAPIView):
    serializer_class = MeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
