
# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie
from .serializers import MovieSerializer
import requests


from django.shortcuts import get_list_or_404, get_object_or_404


API_KEY = 'af5292844a6af1d68203e1c0b3104130'
# API_PAGE = 1
# API_URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-kr&page={API_PAGE}'
# https://api.themoviedb.org/3/movie/top_rated?api_key=af5292844a6af1d68203e1c0b3104130&language=ko-kr&page=1


@api_view(['GET'])
def get_movies_API(request):
    if request.method == 'GET':

        # PAGE_RANGE로 데이터를 가져올 TMDB 페이지를 설정 (최소 1, 최대 500)
        PAGE_RANGE = 20
        for API_PAGE in range(1, PAGE_RANGE):
            API_URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-kr&page={API_PAGE}'


            print(f'{API_PAGE}번 페이지를 불러오는 중')


            # API_URL에 요청하여 얻은 데이터
            movies_API = requests.get(API_URL).json()
            
            # 내부 DB에서 호출한 데이터
            movies_in_db = Movie.objects.all()
            
            # 한 페이지 내에 있는 데이터 분리
            for movie_API in movies_API['results']:

                try:
                    
                    # 불러온 영화의 id가 NULL인 경우 continue
                    if movie_API['id'] is None:
                        continue
                    
                    # 불러온 영화의 id를 기록
                    new_movie_id = movie_API['id']

                    # 불러온 영화의 id가 이미 DB 내에 존재하는 경우
                    if movies_in_db.filter(movie_id=new_movie_id).exists():
                        
                        # 최신 데이터로 덮어쓰는 작업
                        movie_in_db = Movie.objects.get(movie_id=new_movie_id)

                        movie_in_db.adult=movie_API['adult'],
                        movie_in_db.backdrop_path=movie_API['backdrop_path'],
                        movie_in_db.genre_ids=movie_API['genre_ids'],
                        movie_in_db.movie_id=movie_API['id'],
                        movie_in_db.original_language=movie_API['original_language'],
                        movie_in_db.original_title=movie_API['original_title'],
                        movie_in_db.overview=movie_API['overview'],
                        movie_in_db.popularity=movie_API['popularity'],
                        movie_in_db.poster_path=movie_API['poster_path'],
                        movie_in_db.release_date=movie_API['release_date'],
                        movie_in_db.title=movie_API['title'],
                        movie_in_db.video=movie_API['video'],
                        movie_in_db.vote_average=movie_API['vote_average'],
                        movie_in_db.vote_count=movie_API['vote_count'],
      
                        # 완료 후 다음 영화 데이터로 이동
                        continue


                    # DB 내에 존재하지 않는 데이터를 추가
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
                        vote_count=movie_API['vote_count'],
                    )

                    # 새로운 데이터를 저장
                    movie.save()

                except Exception as err:
                    return Response({"result": "Error", "message": str(err)})

        return Response({"result": "OK"})


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


