"""
웹 스크래핑 기술 코드
: 이를 통해서 크롤링을 통해서 기사들을 수집할수 있는 것 같다.!
출처 : https://auto-trading.tistory.com/entry/%ED%8A%B9%EA%B0%95-%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81Web-Crowling-%EA%B8%B0%EC%B4%88-%EA%B0%9C%EB%85%90%EA%B3%BC-%EC%BD%94%EB%93%9C-%EA%B5%AC%ED%98%84with-Python
"""
from urllib.request import urlopen

from bs4 import BeautifulSoup

res = urlopen('https://n.news.naver.com/mnews/article/020/0003497092?sid=105')

soup = BeautifulSoup(res, 'html.parser')

value = soup.find('div', {"id": "dic_area"})
value2 = value.text.strip()
print(value2)