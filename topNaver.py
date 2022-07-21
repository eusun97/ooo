################# top5_page
from email import header
import urllib.request
from wsgiref import headers
from bs4 import BeautifulSoup as bs, Script
from requests import request
import requests
import pandas as pd

def one_page_list(sosok, page):
   
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1" #주소설정

    html = bs(requests.get(url,headers={'User-agent':'Mozilla/5.0'}).text,"lxml")
    global STOCK_NAME_LIST
    STOCK_NAME_LIST = []
    STOCK_PRICE_LIST = []
    top=0
    priceTop=0
    for tr in html.findAll('tr'):
        stockName = tr.findAll('a', attrs={'class', 'tltle'})
        if stockName is None or stockName == []:
            pass
        else:
            top=top+1
            if(top==6):
                break
            stockName = stockName[0].contents[-1]
            STOCK_NAME_LIST.append(stockName)
 
        stockPrice = tr.findAll('td', attrs={'class', 'number'})
        if stockPrice is None or stockPrice == []:
            pass
        else:
            priceTop=priceTop+1
            if(priceTop==6):
                break
            stockPrice = stockPrice[0].contents[-1]
            stockPrice = stockPrice.replace(",","")
            STOCK_PRICE_LIST.append(stockPrice)
            
    STOCK_LIST = []
    
    for i in range(len(STOCK_NAME_LIST)):
        stockInfo = [STOCK_NAME_LIST[i], int(STOCK_PRICE_LIST[i])]
        STOCK_LIST.append(stockInfo)
        print(stockInfo)
        df = pd.DataFrame(STOCK_LIST, columns=('종목명','현재가'))
        js = df.to_json(orient='columns').encode().decode('unicode-escape')   
    return js

one_page_list(1, 1)