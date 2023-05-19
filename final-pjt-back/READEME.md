### migration 지우기

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
rm db.sqlite3



### loaddate 쓰기 

python manage.py makemigrations
python manage.py migrate
python manage.py runserver



### TMDB Image API 링크
f'https://image.tmdb.org/t/p/original/{backdrop_path}'
f'https://image.tmdb.org/t/p/original/{poster_path}'

https://image.tmdb.org/t/p/original/tmU7GeKVybMWFButWEGl2M4GeiP.jpg



### 오늘의 할일 5.19.
1. ---------------- 토큰 가져오는 걸로 유저를 연동
2. Popular movie 쏴주는 view 만들기
3. 좋아요 댓글 만들고
4. 이것도 유저 연동



### 시행착오와 생각

1. movies > models.py > Movie
- Q. 받아오는 Movie의 ID를 Primary key로 지정해주는 것이 좋을까?
  - ID를 Primary key로 저장하면 DB 내에서 자동적으로 기본키를 기준으로 정렬한다. 그런데 데이터는 평점 순으로 정렬된 상태이므로, 추후에 다시 정렬을 해줘야하는 안타까운 상황이 발생하므로, movie_ID를 기본키로 설정하지 않는다. 근데 물리적인 차이가 있는 것인지는 모르겠다.


2. movies > views.py > get_movies_API
- Q. 수정하기 vs 모두 지우고 다시 기록하기
  - 후자가 편리하고 빠르다. 수정할 부분을 찾는 작업을 하느니 다시 쓰는 것이 나을 수도 있는 것 같다. 특히 데이터가 쌓일수록 불일치 검색을 하는 시간이 늘어난다.

- Q. **movie_API?
  - 필드에 각각 값을 넣어주는 것과 결과가 다르게 나온다. 하나씩 지정해주는 게 좀 더 안정적이지 않을까















