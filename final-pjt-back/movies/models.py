from django.db import models

# Create your models here.


class Movie(models.Model):
    
    adult = models.TextField()
    backdrop_path = models.TextField()
    genre_ids = models.TextField()
    movie_id = models.IntegerField()
    original_language = models.TextField()
    original_title = models.TextField()
    overview = models.TextField()
    popularity = models.IntegerField()
    poster_path = models.TextField()
    release_date = models.TextField()
    title = models.TextField()
    video = models.TextField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()


    # total = models.JSONField()
