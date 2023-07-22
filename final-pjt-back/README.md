
### 초기 설정
<!-- 가상 환경 설정 -->
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt


### Migration 및 실행
python manage.py makemigrations
python manage.py migrate


<!-- 초기 데이터 fixture 불러오기 -->
python manage.py loaddata initial_data.json

<!-- 초기 데이터 fixture 저장할 때는 이렇게 -->
PYTHONIOENCODING=utf8 python manage.py dumpdata > initial_data.json


<!-- Top rated 주기적인(60분) loading 없는 runserver -->
python manage.py runserver

<!-- Top rated 주기적인(60분) loading 있는 runserver -->
python manage.py start_server


### Migration 지우기
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
rm db.sqlite3



### 시행착오와 생각 메모
1. 받아오는 Movie의 ID를 Primary key로 지정해주는 것이 좋을까? (movies > models.py > Movie)
 - ID를 Primary key로 저장하면 DB 내에서 자동적으로 기본키를 기준으로 정렬한다. 그런데 데이터는 평점 순으로 정렬된 상태이므로, 추후에 다시 정렬을 해줘야하는 안타까운 상황이 발생하므로, movie_ID를 기본키로 설정하지 않는다. 

2. 수정하기 vs 모두 지우고 다시 기록하기 (movies > views.py > get_movies_API)
 - 후자가 편리하고 빠르다. 수정할 부분을 찾는 작업을 하느니 다시 쓰는 것이 나을 수도 있는 것 같다. 특히 데이터가 쌓일수록 불일치 검색을 하는 시간이 늘어난다.

3. **movie_API? (movies > views.py > get_movies_API)
 - 필드에 각각 값을 넣어주는 것과 결과가 다르게 나온다. 하나씩 지정해주는 게 좀 더 안정적이지 않을까

4. back_api > settings.py 와 dj_rest_auth
- 다 해놓고 settings 설정을 안해서 많이 돌아갔다.
- dj_rest_auth를 사용하는 것이 꽤 까다로웠다. 공식 문서를 잘 참고해야한다.

5. (해결) 커뮤니티 기능
- 댓글 달 때와 좋아요 누를 때 페이지를 reload 하는 문제
- 다른 유저가 입력하는 정보도 받아와야하니까 맞는 것 같기도한데 자원 소모가 심할 것 같은데.. 비동기 처리를 알아봐야할 것 같다
- 뷰 이동이랑 데이터 흐름이 얼기설기 얽혀서 정리를 해봐야겠다

6. (해결) 영화 좋아요를 만들긴 했는데...
- 로그아웃하고 로그인하면 좋아요 눌렀던 게 하얗게 나오는 문제가 있다
- 상위 컴포넌트에서 하위로 id를 넘기고 그걸로 표시를 해야하는 것 같은디...

7. git과 github 사용을 하고 있는데
- 지금은 branch merge만 사용하고 있지만 기능이 꽤나 다양한 듯하다.
- branch에서 작업하는 것을 잊어버리면 조금 번거로워질 수 있다

8. 낱말판 알고리즘
- 낱말 판을 준다.
  - 자주 쓰이는 단어에 무작위 셔플을 해 본 결과. 유효한 단어가 만들어지기가 힘들다. 따라서, 정해진 여러 개의 판 중 하나를 표출하는 것으로 설정
     
- 단어를 최대 3개 입력받는다.
  - 낱말에 좌표를 주고 클릭 결과에 따른 방향을 기록하여 단방향으로만 단어를 형성할 수 있도록 제한

- 제출하고 결과를 돌려준다.
  - 단어 리스트에 대해서 Search API를 돌린다. 결과가 없으면 Now Playing을 반환
  - 매번 같은 결과가 나오면 재미없으니까 조금 더 받아서 랜덤으로 일부만 주는 방식 (10개 중 3개 랜덤 이런 식으로)


