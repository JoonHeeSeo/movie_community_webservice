### migration 지우기

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
rm db.sqlite3



### loaddate 쓰기 

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


