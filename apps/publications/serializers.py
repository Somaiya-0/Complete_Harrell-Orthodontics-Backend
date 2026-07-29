from rest_framework import serializers
from .models import Publication, Event


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ["id", "title", "kind", "authors", "year", "url"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "kind", "audience", "starts_at", "location", "fee", "registration_url"]
