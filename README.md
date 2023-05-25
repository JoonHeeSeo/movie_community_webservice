# Final Project
Final-PJT of 1st semester in SSAFY


## 1. 팀원 정보 및 업무 분담 내역
- (팀장) 최현우 : 주로 front server
- (팀원) 서준희 : 주로 back-api

## 2. 목표 서비스 구현 및 실제 구현 정도
- 목표 : 로그인이 최소화된 영화추천 서비스, 로그인 사용자는 커뮤니티 서비스 및 평점 기능 이용 가능
- 구현 : 영화 커뮤니티 서비스

## 3. 데이터베이스 모델링 
<img src="./erd_total.PNG" alt="erd_total" width="60%" height="60%">
<img src="./erd_simple.PNG" alt="erd_simple" width="60%" height="60%">

## 4. 영화 추천 알고리즘에 대한 기술적 설명
 1. 적절한 낱말판을 배치한다.
 2. 관련 단어를 최대 3개 입력 받는다.
 3. 단어에 대한 결과를 TMDB API에 요청하여 결과를 돌려준다.

## 5. 서비스 대표 기능에 대한 설명
- 커뮤니티 기능 (글, 댓글, 좋아요)
- 회원 기능 (가입, 로그인, 프로필)
- 영화 조회 (상영작, 검색, 추천)

## 6. 배포 서버 URL (배포 했을 경우)
- 아직

## 7. 기타 느낀점 후기 등
- [개발 과정 README](./final-pjt-back/README.md)




### Records
23.05.17.
- Django Startproject, startapp,
- Vue add Vuex, Router
- 스켈레톤 코드 제작
- TMDB API 받아오는 방식 확인 


23.05.18.
- 새로운 브랜치 만들어서 작업
- 회원가입, 로그인 방법 구현
- (token 발행 및 User인증정보를 localStorage에 저장)
<b> -> 안전하지 않은 방법이라는 것을 인지하고 있으므로, 대체 할 수 있는 방법 업데이트 예정</b>


23.05.19.
Community 
-back(준희)
- vue와 django 간의 유저 정보 연동
- 게시글 상세 보기 및 댓글 보기 기능 구현(작성자 및 작성시간 함께 표시)

-front(현우)
- 입력된 input text로 영화검색기능 달기 vuex axios를 통해 api연동
(유사 단어를 처리 못하는 문제 발생)
- NAV bar, signin, signup style 구성
(view내의 모든 파일에 적용되는 문제 발생)


