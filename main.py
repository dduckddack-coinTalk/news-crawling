import crawling
import mongoDB

news = crawling.news_crawling()
mongoDB.insert_news(news)
