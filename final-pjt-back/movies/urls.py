from django.urls import path
from . import views


urlpatterns = [
    path('get', views.get_movies_API),
    path('', views.movie_list),
]
