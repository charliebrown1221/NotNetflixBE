from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from authentication.models import User
from movies.models import Movies
from movies.serializers import MoviesSerializer

# Create your views here.
@api_view([ 'GET'])
@permission_classes([IsAuthenticated])
def get_all_favorite_movie(request):
    user = User.objects.get(pk=request.user.id)
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if  request.method == 'GET':
          movie = user.favorites.all()
          serializer = MoviesSerializer(movie,many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)
  
  
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorite_movie(request, movie_id):
   movie=Movies.objects.get(pk=movie_id)
   user = User.objects.get(pk = request.user.id)
   print(request.user.id)
   if request.method == 'POST':
      movie.favorites.add(user)
      serializer = MoviesSerializer(movie, many=False)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_favorite_movie(request, movie_id):
   movie=Movies.objects.get(pk=movie_id)
   user = User.objects.get(pk = request.user.id)
   print(request.user.id)
   if request.method == 'DELETE':
      movie.favorites.remove(user)
      return Response( status=status.HTTP_204_NO_CONTENT)
   return Response(status=status.HTTP_400_BAD_REQUEST)
