from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list),
    path('get/movies/', views.get_movies_API),
    path('get/movies_search/<movie_name>/', views.get_movies_search_API),
    path('get/movie_detail/<movie_id>/', views.get_movie_detail_API),
    path('get/now_playing_movies/', views.get_now_playing_movies_API),
    path('get/upcoming_movies/', views.get_upcoming_movies_API),

    path('profile/<str:username>/', views.profile_get),
    path('<int:movie_id>/likes/', views.movie_likes),
    path('recommend/', views.movie_recommend),

    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:movie_id>/comments/get/', views.comment_get),
    path('<int:movie_id>/comments/create/', views.comment_create),

    


]
