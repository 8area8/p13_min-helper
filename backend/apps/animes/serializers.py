"""Animes serializers."""

from rest_framework import serializers
from .models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    """Animes serializer."""

    categories = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = Anime
        fields = "__all__"