from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 유저 '좋아요'를 누를 영화의 ID를 JSON 형식으로 저장
    like_movies = models.JSONField(default=list)


