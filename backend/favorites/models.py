from django.db import models
from movies.models import Movies
from authentication.models import User


# Create your models here.
class FavoriteMovies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie =models.ManyToManyField(Movies)