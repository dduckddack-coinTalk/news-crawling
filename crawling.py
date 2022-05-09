import requests
from bs4 import BeautifulSoup

print('뉴스기사 스크래핑 시작')

index = 1
list = []
newsDomain = "https://www.coindeskkorea.com"

while index < 2:
    url = "https://www.coindeskkorea.com/news/articleList.html?page="+str(index)+"&total=11166&box_idxno=&view_type=sm"
    req = requests.get(url)
    req.encoding = None
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.select(
        'div.list-block'
    )



    for data in datas:
        title = data.select_one("div.text-block > div.list-titles").text.strip()  # 제목

        style = data.select_one("div.list-block > div.list-image")["style"]
        imgUrl = newsDomain + "/news" + style[style.find("./") +1 :-1]

        editorCreatedAt = data.select_one("div.text-block > div.list-dated").text.strip()  # 작성자 + 작성일
        createdAt = editorCreatedAt[editorCreatedAt.find(' ') + 1:]  # 작성일
        editor = editorCreatedAt[:editorCreatedAt.find(' ')]  # 작성자

        summary = data.select_one("div.text-block > p.list-summary").text.strip()  # 본문
        newUrl = newsDomain + data.select_one("div.text-block > p.list-summary >a ")["href"]  # link

        list.append({
            "title": title,
            "editor": editor,
            "createdAt": createdAt,
            "summary": summary,
            "url": url
        })

    index += 1

print('뉴스기사 스크래핑 끝')
