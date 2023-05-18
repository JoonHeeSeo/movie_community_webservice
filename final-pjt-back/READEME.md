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
