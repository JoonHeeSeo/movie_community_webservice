from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list),
    path('get/movies/', views.get_movies_API),
    path('get/movies_search/<movie_name>/', views.get_movies_search_API),
    path('get/movie_detail/<movie_id>/', views.get_movie_detail_API),
    path('get/now_playing_movies/', views.get_now_playing_movies_API),
    path('get/upcoming_movies/', views.get_upcoming_movies_API),

    path('<int:movie_id>/likes/', views.movie_likes),
    path('profile/<str:username>/', views.profile_get),
]
