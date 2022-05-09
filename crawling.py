import requests
from bs4 import BeautifulSoup

print('뉴스기사 스크래핑 시작')


req = requests.get('https://www.coindeskkorea.com/news/articleList.html?page=2&total=11166&box_idxno=&view_type=sm')
req.encoding = None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    'div.list-block'
)

list = []

for data in datas:
    title = data.select_one("div.text-block > div.list-titles").text.strip()  # 제목
    editorCreatedAt = data.select_one("div.text-block > div.list-dated").text.strip()  # 작성자 + 작성일
    createdAt = editorCreatedAt[editorCreatedAt.find(' ') + 1:]  # 작성일
    editor = editorCreatedAt[:editorCreatedAt.find(' ')]  # 작성자
    summary = data.select_one("div.text-block > p.list-summary").text.strip()  # 본문
    url = data.select_one("div.text-block > p.list-summary >a ")["href"]  # link

    list.append({
        "title": title,
        "editor": editor,
        "createdAt": createdAt,
        "summary": summary,
        "url": url
    })

print('뉴스기사 스크래핑 끝')
