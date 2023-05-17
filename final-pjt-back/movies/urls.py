from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_movies_API),
    # path('<int:movie_pk>', views.movie_detail),
]
