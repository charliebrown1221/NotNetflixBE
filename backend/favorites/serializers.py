from dataclasses import fields
from rest_framework import serializers
from .models import FavoriteMovies


class FavoriteMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovies
        fields =['id','user_id','movie']
        depth = 1