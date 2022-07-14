from wsgiref import headers
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import pandas as pd



url= 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'

html = BeautifulSoup(requests.get(url,headers={'User-agent':'Mozilla/5.0'}).text,"lxml")
        #뷰티풀수프 생성자의 첫번째 인수로 HTML/XML페이지의 파일경로나 URL,두번째인수로 웹페이지를 파싱할 방식


pgrr = html.find('td', class_='pgRR')    #class속성이 pgRR인 td태그 찾으면,결과값은 bs4.element.Tag타입으로prgg에 반환.pgRR은 맨오른쪽페이지를 의미
s=str(pgrr.a['href']).split('=')
# s는 ['/item/sise_day.nhn?code', '068270&page','351'] 의 3개 문자열을 리스트로 얻었다. =로 분리함
last_page = s[-1]
print(last_page)




df = pd.DataFrame()         #일별시세를 저장할 df변수가 데이터프레임형임을 인터프린터에 알림
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'

for page in range(1, int(last_page)+1):         #1부터 마지막페이지까지 반복
    page_url = '{}&page={}'.format(sise_url, page)
    html = requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text
    table = pd.read_html(html)
    df = df.append(table[0])  #read_html()함수로 읽은 한 페이지 분량의 데이터프레임 df객체에 추가
    # df = df.append(pd.read_html(page_url,header=0, encoding='cp949')[0])  #read_html()함수로 읽은 한 페이지 분량의 데이터프레임 df객체에 추가

df=df.dropna()      #값이 빠진 행 제거
print(df)