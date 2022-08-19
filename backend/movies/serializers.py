from dataclasses import fields
from rest_framework import serializers
from .models import  Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields =["id",'user', 'name','overview','year','genres','poster_path','fileName']
        depth = 1
    
        



