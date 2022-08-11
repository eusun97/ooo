################# top5_page

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

def one_page_list(sosok, page):
   
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1" #주소설정

    html = bs(requests.get(url,headers={'User-agent':'Mozilla/5.0'}).text,"lxml")
    global STOCK_NAME_LIST
    global STOCK_CODE_LIST
    STOCK_NAME_LIST = []
    STOCK_PRICE_LIST = []
    STOCK_CODE_LIST = []
    top=0
    priceTop=0

    table = html.find_all("table", {"class": "type_2"})[0]

    for tr in table.findAll('tr'):
        stockName = tr.findAll('a', attrs={'class', 'tltle'})
        if stockName is None or stockName == []:
            pass
        else:
            top=top+1
            if(top==6):
                break
            STOCK_NAME_LIST.append(stockName[0].contents[-1])
            STOCK_CODE_LIST.append(stockName[0]["href"].split("code=")[-1])
 
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
        stockInfo = [STOCK_NAME_LIST[i], int(STOCK_PRICE_LIST[i]), STOCK_CODE_LIST[i]]
        STOCK_LIST.append(stockInfo)
        df = pd.DataFrame(STOCK_LIST, columns=('종목명','현재가',"code"))
        js = df.to_json(orient='columns').encode().decode('unicode-escape')   
    return js

one_page_list(1, 1)

