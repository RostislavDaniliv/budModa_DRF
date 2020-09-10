from rest_framework import serializers
from .models import *


class TypePageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePage
        fields = ("name",)


class PageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        exclude = ("background_img", )

    categories = serializers.SlugRelatedField(slug_field="name", read_only=True)


class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ("id", "title_m")