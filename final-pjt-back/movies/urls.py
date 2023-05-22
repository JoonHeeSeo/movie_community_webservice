from django.urls import path
from . import views


urlpatterns = [
    path('get/movies/', views.get_movies_API),
    # path('get/movie_detail/', views.get_movie_detail_API),
    path('get/movies_search/', views.get_movies_search_API),
    path('get/now_playing_movies/', views.get_now_playing_movies_API),
    path('get/upcoming_movies/', views.get_upcoming_movies_API),
    path('', views.movie_list),
]
