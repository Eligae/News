import requests
from bs4 import BeautifulSoup as bs

def getPages():
    pages = requests.get("https://news.naver.com/")
    soup = bs(pages.content, 'html.parser')

    target_links = soup.find_all('a', href=lambda value: value and '/main/main.naver?mode=LSD&mid=shm&sid1=' in value)

    values_dict = {}

    for link in target_links:
        value = link['href'].split('/main/main.naver?mode=LSD&mid=shm&sid1=')[-1]
        text = link.get_text(strip=True) 
        values_dict[value] = text




