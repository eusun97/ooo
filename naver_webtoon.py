from turtle import title
from bs4 import BeautifulSoup
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday")

soup = BeautifulSoup(html.text,'html.parser')
html.close()

monday = soup.find('div',{'class':'col_inner'})

title = monday.findAll('img')


tt=title[0]['title']

for name in title:
    print(name['title'])




