# final-pjt
Final-pjt first semester in SSAFY
<br>

### i. 팀원 정보 및 업무 분담 내역
최현우 서준희
<br>
230517 스켈레톤 코드 제작 및 api 연결
네비게이터: 서준희 드라이버: 최현우
업무 내용: 지시와 이행 
<br>

### ii. 목표 서비스 구현 및 실제 구현 정도
로그인이 최소화된 영화추천 서비스 
(로그인 사용자는 커뮤니티 서비스 및 평점 기능 이용 가능)

### iii. 데이터베이스모델링 

ERD 추후 추가 예정 

### iv. 영화 추천 알고리즘에 대한 기술적 설명

### v. 서비스 대표 기능에 대한 설명

### vi. 배포 서버 URL (배포했을 경우)

### vii. 기타 느낀 점 후기 등


## Records

23.05.17
- Django Startproject, startapp,
- Vue add Vuex, Router
- 스켈레톤 코드 제작
- TMDB API 받아오는 방식 확인 

23.05.18.
- 새로운 브랜치 만들어서 작업
- 회원가입, 로그인 방법 구현
- (token 발행 및 User인증정보를 localStorage에 저장)
<b> -> 안전하지 않은 방법이라는 것을 인지하고 있으므로, 대체 할 수 있는 방법 업데이트 예정</b>

Community 
-back(준희)
- vue와 django 간의 유저 정보 연동
- 게시글 상세 보기 및 댓글 보기 기능 구현(작성자 및 작성시간 함께 표시)

-fron(현우)
- 입력된 input text로 영화검색기능 달기 vuex axios를 통해 api연동
(유사 단어를 처리 못하는 문제 발생)
- NAV bar, signin, signup style 구성
(view내의 모든 파일에 적용되는 문제 발생)