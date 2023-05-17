
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie
import requests



API_KEY = 'af5292844a6af1d68203e1c0b3104130'
API_PAGE = 1
API_URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-kr&page={API_PAGE}'


@api_view(['GET'])
def get_movies_API(request):
    if request.method == 'GET':

        # API_URL에 요청하여 얻은 데이터
        movies_API = requests.get(API_URL).json()
        
        # 내부 DB에서 호출한 데이터
        movies_in_db = Movie.objects.all()
        
        # 한 페이지 내에 있는 데이터 분리
        for movie_API in movies_API['results']:

            try:
                # 불러온 영화의 id를 기록
                movie_id = movie_API['id']
                # 불러온 영화의 id가 이미 DB 내에 존재하는 경우 continue
                if movies_in_db.filter(movie_id=movie_id).exists():
                    continue

                # 데이터 형식과 일치 (id는 규칙에 의해 movie_id로 변경)
                movie = Movie(
                    adult=movie_API['adult'],
                    backdrop_path=movie_API['backdrop_path'],
                    genre_ids=movie_API['genre_ids'],
                    movie_id=movie_API['id'],
                    original_language=movie_API['original_language'],
                    original_title=movie_API['original_title'],
                    overview=movie_API['overview'],
                    popularity=movie_API['popularity'],
                    poster_path=movie_API['poster_path'],
                    release_date=movie_API['release_date'],
                    title=movie_API['title'],
                    video=movie_API['video'],
                    vote_average=movie_API['vote_average'],
                    vote_count=movie_API['vote_count']
                )

                movie.save()

            except Exception as e:
                return Response({"result": "Error", "message": str(e)})

        return Response({"result": "OK"})

