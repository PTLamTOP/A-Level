from rest_framework import serializers
from filmsessions.models import FilmSession, Film


class FilmSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmSession
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
