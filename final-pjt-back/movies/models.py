from django.db import models

# Create your models here.


class Movie(models.Model):
    

    # movie_id를 제외한 모든 필드 null과 blank 허용
    adult = models.TextField(null=True, blank=True)
    backdrop_path = models.TextField(null=True, blank=True)
    genre_ids = models.TextField(null=True, blank=True)
    movie_id = models.IntegerField(null=True, blank=True)
    original_language = models.TextField(null=True, blank=True)
    original_title = models.TextField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    poster_path = models.TextField(null=True, blank=True)
    release_date = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    video = models.TextField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)


