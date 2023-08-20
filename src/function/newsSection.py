import requests
from bs4 import BeautifulSoup as bs
import re
import os

import var    # for global variable

# naver news에 분야별 값 빼오기
# return as {"경제": 100, "정치": 101,...}
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

# naver news의 분야에 해당하는 뉴스 기사 긁어오기
# return as ['URL1', 'URL2'...]
def getNewsLinks(genre):
    url = f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={genre}"
    pages = requests.get(url, headers=var.headers)
    soup = bs(pages.content, 'html.parser')
    
    pattern = re.compile(r"https://n\.news\.naver\.com/mnews/article/")
    
    article_links = set()

    for link in soup.find_all('a', href=True):
        if pattern.search(link['href']):
            article_links.add(link['href'])
    
    return list(article_links)

# URL에 해당하는 기사내용만 가져오기(img 제외)
# return as string
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
    
def saveTextToFolder(text, path, fileName):
    if not os.path.exists(path):
        os.makedirs(path)
    path = os.path.join(path, fileName)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

i = 1    
valuesDict = getPages()
for key, value in valuesDict.items():
    link = getNewsLinks(value)
    print(f'doing link {key} : {value}..')
    for url in link:
        article = getArticle(url)
        articleRe = article.replace('.', '\n')
        print(f'saving to \\DATA\\{key[0]}...')
        saveTextToFolder(articleRe, f'.\\DATA\\{key}', f'{i}.txt')
        i += 1
    i = 1