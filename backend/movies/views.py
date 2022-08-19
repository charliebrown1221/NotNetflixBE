from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Movies
from .serializers import  MoviesSerializer





@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_movies(request ):
    if  request.method == 'GET':
       movie = Movies.objects.all()
    serializer = MoviesSerializer(movie,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_movie(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view([ 'PUT'])
@permission_classes([IsAuthenticated])
def edit_movie(request, pk):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    movie=get_object_or_404(Movies,pk=pk,)
    if request.method == 'PUT':
         serializer= MoviesSerializer(movie,data=request.data)
         if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view([ 'DELETE'])
@permission_classes([IsAuthenticated])
def delete_movie(request, pk):
 movie=get_object_or_404(Movies,pk=pk,)
 if request.method == 'DELETE':
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




