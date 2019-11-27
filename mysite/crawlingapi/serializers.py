from .models import MovieInfo
from rest_framework import serializers

class MovieInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieInfo
        field = '__all__'