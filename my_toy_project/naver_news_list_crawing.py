"""
네이버 경제 기사 웹 스크래핑
"""
from urllib.request import urlopen

from bs4 import BeautifulSoup

response = urlopen("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101")

soup = BeautifulSoup(response, 'html.parser')
value = soup.find("ul", {"class":"sh_list"})

newArray = value.select("li", {"class": "sh_item _cluster_content"})
for index, item in enumerate(newArray) :
    print(f"======================{index}================")
    headline = item.find("a", {"class": "sh_text_headline"})
    aLink = headline["href"]
    headLineTitle = headline.text
    print(f"{headLineTitle} : {aLink}")