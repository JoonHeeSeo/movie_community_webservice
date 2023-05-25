
import requests
import random

from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Comment
from accounts.models import User
from .serializers import MovieSerializer, CommentSerializer, UserSerializer


import time

API_KEY = 'af5292844a6af1d68203e1c0b3104130'


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_movies_API(request):
    if request.method == 'GET':


        start_time = time.time()

        # Movie 데이터 초기화
        Movie.objects.all().delete()

        # PAGE_RANGE로 데이터를 가져올 TMDB 페이지를 설정 (최소 1, 최대 500)
        PAGE_RANGE = 30
        for API_PAGE in range(1, PAGE_RANGE + 1):

            API_URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-kr&page={API_PAGE}'
                        # https://api.themoviedb.org/3/movie/top_rated?api_key=af5292844a6af1d68203e1c0b3104130&language=ko-kr&page=1

            print(f'{API_PAGE}번 페이지를 불러오는 중')

            # API_URL에 요청하여 얻은 데이터
            movies_API = requests.get(API_URL).json()
            
            # 한 페이지 내에 있는 데이터 분리
            for movie_API in movies_API['results']:

                try:
                    # 새로운 데이터를 저장
                    # movie = Movie(movie_id=movie_API['id'], **movie_API)
                    # movie = Movie(**movie_API)

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

                    movie.save()


                except Exception as err:
                    return Response({"result": "Error", "message": str(err)})



        print(time.time() - start_time)



        return Response({"result": "OK"})


@api_view(['GET'])
def get_movies_search_API(request, movie_name):
    if request.method == 'GET':
        SEARCH_INPUT = movie_name
        API_URL = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={SEARCH_INPUT}&language=ko-kr'
        searched_movies_API = requests.get(API_URL).json()
        return Response(searched_movies_API['results'])
    

@api_view(['GET'])
def get_movie_detail_API(request, movie_id):
    if request.method == 'GET':
        MOVIE_ID = movie_id
        API_URL = f'https://api.themoviedb.org/3/movie/{MOVIE_ID}?api_key={API_KEY}&language=ko-kr'
        # API_URL = f'https://api.themoviedb.org/3/movie/11?api_key=af5292844a6af1d68203e1c0b3104130&language=ko-kr'
        movie_detail_API = requests.get(API_URL).json()
        return Response(movie_detail_API)


@api_view(['GET'])
def get_now_playing_movies_API(request):
    if request.method == 'GET':
        API_PAGE = 1
        API_URL = f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko-kr&page={API_PAGE}'
        now_playing_movies_API = requests.get(API_URL).json()
        return Response(now_playing_movies_API['results'])


@api_view(['GET'])
def get_upcoming_movies_API(request):
    if request.method == 'GET':
        API_PAGE = 1
        API_URL = f'https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=ko-kr&page={API_PAGE}'
        upcoming_movies_API = requests.get(API_URL).json()
        return Response(upcoming_movies_API['results'])


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_get(request, username):

    user = User.objects.get(username=username)
    serializer = UserSerializer(user)

    movies = []
    for MOVIE_ID in serializer.data['like_movies']:
        API_URL = f'https://api.themoviedb.org/3/movie/{MOVIE_ID}?api_key={API_KEY}&language=ko-kr'
        movie_detail_API = requests.get(API_URL).json()
        movies.append( { 'movie_id':MOVIE_ID, 'title': movie_detail_API['title'] })

    comments = Comment.objects.filter(user_id=user.id)
    updated_comments = []

    for comment in comments:
        MOVIE_ID = comment.movie_id
        API_URL = f'https://api.themoviedb.org/3/movie/{MOVIE_ID}?api_key={API_KEY}&language=ko-kr'
        movie_detail_API = requests.get(API_URL).json()
        comment_data = {
            'id': comment.id,
            'movie_id': MOVIE_ID,
            'content': comment.content,
            'created_at': comment.created_at,
            'updated_at': comment.updated_at,
            'user_id': comment.user_id,
            'title': movie_detail_API['title']
        }
        updated_comments.append(comment_data)

    profile_data = {'movies': movies, 'comments': updated_comments}
    return Response(profile_data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_likes(request, movie_id):
    if request.method == 'GET':
        user = User.objects.get(username=request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data['like_movies'])

    elif request.method == 'POST':
        user = User.objects.get(username=request.user)
        
        if movie_id in user.like_movies:
            user.like_movies.remove(movie_id)
        else:
            user.like_movies.append(movie_id)

        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data['like_movies'])



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_recommend(request):

    recommend_movies = []
    for SEARCH_INPUT in request.data['resultInput']:
        API_URL = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={SEARCH_INPUT}&language=ko-kr'
        searched_movies_API = requests.get(API_URL).json()
        
        for idx in range(3):
            try:
                recommend_movies.append(searched_movies_API['results'][idx])
            except:
                pass
    
    if len(recommend_movies) < 3:
        API_PAGE = 1
        API_URL = f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko-kr&page={API_PAGE}'
        now_playing_movies_API = requests.get(API_URL).json()

        for movie_data in now_playing_movies_API['results']:
            recommend_movies.append(movie_data)

    random.shuffle(recommend_movies)
    return Response(recommend_movies[:3])



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def comment_get(request, movie_id):
    comments = Comment.objects.filter(movie_id=movie_id)

    serializer = []
    for comment in comments:
        serializer.append({
            'id': comment.id,
            'content': comment.content,
            'created_at': comment.created_at,
            'updated_at': comment.updated_at,
            'user': comment.user.username,
        })

    return Response(serializer)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_id):
    content = request.data['content']
    comment = Comment(movie_id=movie_id, content=content, user=request.user)

    try:
        comment.save()
        return Response({"result": "OK"})

    except Exception as e:
        return Response({"result": str(e)})



