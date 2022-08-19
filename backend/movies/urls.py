from django.urls import path
from . import views

urlpatterns =[
    path('all/', views.get_all_movies),
    path('add/', views.add_movie),  
    path('edit/<int:pk>', views.edit_movie),  
    path('delete/<int:pk>', views.delete_movie),  
     



]

