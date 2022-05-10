import crawling
import mongoDB

news = crawling.news_crawling()
mongoDB.insert_news(news)
#todo(github issue 등록으로 알림 받기)