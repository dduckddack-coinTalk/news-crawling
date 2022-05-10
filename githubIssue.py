import os
from github import Github, Issue
from datetime import datetime


def make_issue(news):
    ISSUE_TOKEN = os.environ['ISSUE_TOKEN']
    title = datetime.now() + "뉴스 크롤링"
    body = news
    REPO_NAME = 'https://github.com/dduckddack-coinTalk/news-crawling.git'

    g = Github(ISSUE_TOKEN)
    repo = Github(ISSUE_TOKEN).get_user().get_repo(REPO_NAME)
    repo = g.get_organization("dduckddack-coinTalk").get_repo("news-crawling")

    repo.create_issue(title=title, body=body)
