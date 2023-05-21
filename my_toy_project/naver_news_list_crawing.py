"""
네이버 경제 기사 웹 스크래핑
"""
from urllib.request import urlopen

from bs4 import BeautifulSoup
from openpyxl import Workbook

naver_news_sidList = [
    {"name": "정치", "sid": 100},
    {"name": "경제", "sid": 101},
    {"name": "사회", "sid": 102},
    {"name": "생활/문화", "sid": 103},
    {"name": "IT/과학", "sid": 105}
]


write_wb = Workbook()
sheet = write_wb.active
sheet.title = "테스트"
seq = 1
for newsAgenda in naver_news_sidList :
    response = urlopen(f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={newsAgenda.get('sid')}")

    soup = BeautifulSoup(response, 'html.parser')
    value = soup.find("ul", {"class":"sh_list"})

    newArray = value.select("li", {"class": "sh_item _cluster_content"})
    for index, item in enumerate(newArray) :
        headline = item.find("a", {"class": "sh_text_headline"})
        aLink = headline["href"]
        headLineTitle = headline.text
        sheet.append([seq, headLineTitle, aLink])
        print(f"{headLineTitle} : {aLink}")
        seq = seq + 1


write_wb.save("20230521.xlsx")