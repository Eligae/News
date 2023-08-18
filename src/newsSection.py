import requests
from bs4 import BeautifulSoup as bs
import re

import var    # for global variable

def getPages():
    pages = requests.get("https://news.naver.com/")
    soup = bs(pages.content, 'html.parser')
    target_links = soup.find_all('a', href=lambda value: value and '/main/main.naver?mode=LSD&mid=shm&sid1=' in value)

    values_dict = {}

    for link in target_links:
        value = link['href'].split('/main/main.naver?mode=LSD&mid=shm&sid1=')[-1]
        text = link.get_text(strip=True) 
        values_dict[text] = value

    return values_dict
    
def getNewsLinks(genre):
    url = f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={genre}"
    pages = requests.get(url, headers=var.headers)
    soup = bs(pages.content, 'html.parser')
    
    pattern = re.compile(r"https://n\.news\.naver\.com/mnews/article/")
    
    article_links = set()  # set 자료형을 사용하여 중복 링크 제거

    for link in soup.find_all('a', href=True):
        if pattern.search(link['href']):
            article_links.add(link['href'])
    
    return list(article_links)  # set을 다시 리스트로 변환하여 반환
  
def getArticle(url):
    pages = requests.get(url, headers=var.headers)
    soup = bs(pages.content, 'html.parser')
    
    article_content = soup.find('article', class_='go_trans _article_content')
    if article_content:
        for img in article_content.find_all('img'):
            img.extract()
        text = article_content.get_text(strip=True)
        return text
    else:
        return "기사 내용 찾기 불가.."