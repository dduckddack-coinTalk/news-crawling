import requests
from bs4 import BeautifulSoup
import mongoDB
from datetime import datetime


def news_crawling():
    print('뉴스기사 스크래핑 시작')

    index = 1
    parsed_news = []
    news_domain = "https://www.coindeskkorea.com"
    saved_last_date = mongoDB.saved_last_date()
    break_flag = False

    while index < 20:
        print(str(index) + "번째 페이지")
        url = "https://www.coindeskkorea.com/news/articleList.html?page=" + str(
            index) + "&total=11166&box_idxno=&view_type=sm"
        req = requests.get(url)
        req.encoding = None
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')

        datas = soup.select('div.list-block')

        for data in datas:
            try:
                created_at, editor, img_url, news_url, summary, title = parsing_news(data, news_domain)
            except:
                print("error 발생")

            created_at_to_date = datetime.strptime(created_at, '%Y-%m-%d %H:%M')
            saved_last_date_to_date = datetime.strptime(saved_last_date, '%Y-%m-%d %H:%M')

            if created_at_to_date <= saved_last_date_to_date:
                break

            parsed_news.append({
                "title": title,
                "imgUrl": img_url,
                "editor": editor,
                "createdAt": created_at,
                "summary": summary,
                "url": news_url
            })
        if break_flag:
            break
        index += 1

    print('뉴스기사 스크래핑 끝')

    return parsed_news


def parsing_news(data, news_domain):
    try:
        title = data.select_one("div.text-block > div.list-titles").text.strip()  # 제목
        style = data.select_one("div.list-block > div.list-image")["style"]
        img_url = news_domain + "/news" + style[style.find("./") + 1:-1]
        editor_created_at = data.select_one("div.text-block > div.list-dated").text.strip()  # 작성자 + 작성일
        created_at = editor_created_at[editor_created_at.find('2022'):]  # 작성일
        editor = editor_created_at[:editor_created_at.find('2022') - 1]  # 작성자
        summary = data.select_one("div.text-block > p.list-summary").text.strip()  # 본문
        news_url = news_domain + data.select_one("div.text-block > p.list-summary >a ")["href"]  # link
        return created_at, editor, img_url, news_url, summary, title
    except:
        pass
