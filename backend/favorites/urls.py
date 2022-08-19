from django.urls import path
from . import views

urlpatterns =[
    path('all/', views.get_all_favorite_movie),
    path('add/<int:movie_id>', views.add_favorite_movie), 
    path('delete/<int:movie_id>', views.delete_favorite_movie), 
    
    ]