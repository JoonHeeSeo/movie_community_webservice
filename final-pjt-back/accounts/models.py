from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    like_movies = models.JSONField(default=list)



