# news-crawling

뉴스를 크롤링해서 MongoDB에 저장하는 기능입니다.
<br><br>
## 배경(Background)

뉴스 페이지에서 뉴스리스트를 출력하기 위해 필요한 기능입니다.
<br><br>
## 목표(Goals)

 - 뉴스 크롤링하기
 - 제목, 작성자, 작성일, 썸네일URL, 실제 링크 URL 가져오기
 - 30분 주기로 mongoDB에 저장된 뉴스의 최근 작성일자 이후만 가져와서 저장하기
<br><br>
## 목표가 아닌 것 (Non-goals)

뉴스 본문페이지 구현(저작권 문제로 전체 본문은 가져오지 않음)
<br><br>
## 계획 (Plan)

 - 크롤링 구현
 - Local mongoDB 생성
 - crawling data를 Local mongoDB에 저장
 - AWS mongoDB 생성
 - crawling data를 AWS mongoDB와 연동
 - gitHub Actions로 30분 주기 스케줄 기능 구현
<br><br>
## 이외 고려 사항들(Other Considerations)
