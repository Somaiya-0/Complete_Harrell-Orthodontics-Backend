from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class RoleTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Adds role/name claims to the JWT so the frontend can gate the UI
    without a second request."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["role"] = user.role
        token["name"] = user.get_full_name() or user.username
        return token


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "role", "practice_name", "phone", "is_superuser"]
