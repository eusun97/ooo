import time
from itertools import count
import requests
from email import header
import urllib.request
from wsgiref import headers
from bs4 import BeautifulSoup as bs
from requests import request
import pandas as pd

def one_page_list(sosok, page):
   
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1" #주소설정

    html = bs(requests.get(url,headers={'User-agent':'Mozilla/5.0'}).text,"lxml")

    STOCK_NAME_LIST = []
    STOCK_PRICE_LIST = []

    for tr in html.findAll('tr'):
        stockName = tr.findAll('a', attrs={'class', 'tltle'})
        if stockName is None or stockName == []:
            pass
        else:
            stockName = stockName[0].contents[-1]
            STOCK_NAME_LIST.append(stockName)
            # global top
            # top=top+1
            # if(top==5):
            #     break

        stockPrice = tr.findAll('td', attrs={'class', 'number'})
        if stockPrice is None or stockPrice == []:
            pass
        else:
            stockPrice = stockPrice[0].contents[-1]
            stockPrice = stockPrice.replace(",","")
            STOCK_PRICE_LIST.append(stockPrice)
            #global priceTop
            # priceTop=priceTop+1
            # if(priceTop==5):
            #     break

    STOCK_LIST = []
    
    for i in range(len(STOCK_NAME_LIST)):
        stockInfo = [STOCK_NAME_LIST[i], int(STOCK_PRICE_LIST[i])]
        STOCK_LIST.append(stockInfo)
        # print(stockInfo)
    return pd.DataFrame(STOCK_LIST, columns=('종목명','현재가'))


# naverPage1=one_page_list(1,1)
# naverPage2=naverPage1.sort_values("현재가",axis=0,ascending=False,inplace=True) #axis : {0 : index / 1: columns} 정렬할 레이블입니다. 0이면 행, 1이면 열을 기준으로 정렬합니다.
# naverPage2
# print(naverPage2)



def all_page_list():

    FINAL_LIST = []

    for sosok in range(2):
        for page in range(33):
            one_page_data = one_page_list(sosok, page+1)
            print("{}소속 {}페이지 진행 중 입니다.".format(sosok, page+1))
            
            if one_page_data is None:
                break
            
            FINAL_LIST.append(one_page_data)
            time.sleep(3)
    
    return pd.concat(FINAL_LIST)

#ALL_STOCK_LIST = all_page_list()

