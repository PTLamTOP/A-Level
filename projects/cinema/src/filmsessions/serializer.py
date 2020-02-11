from rest_framework import serializers
from .models import FilmSession


class FilmSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmSession
        fields = '__all__'
