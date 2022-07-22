#########detail_page
from datetime import date, datetime
from operator import index
import FinanceDataReader as fdr
import datetime
import pandas as pd

# 삼성전자(005930)
def prac():
    global d
    d = date(2022, 1, 11)
    
    #d=d+datetime.timedelta(days=2)
    
    global currentStock  

    dat =[]
    df = fdr.DataReader('005930', d.isoformat())
    #print(df.index)
    #print(df)
    
    
    dat=df['Close'].tolist()
    currentStock=dat[-1]
   
    #print(dat)
    indexList= df.index.strftime("%Y-%m-%d").tolist()
    #print(indexList)
    # cal=[]
  
    # for num in range(len(dat)):   # 종가 갯수만큼 반복
        
    #     #print(d.weekday())

    #     if(0 <= d.weekday() <=4): # 평일일 때만 cal[] 에 날짜를 삽입함
    #         print(d.weekday())

    #         cal.append(d)           # 문제가, for문은 정해진 갯수만큼 계속 반복을 함, 근데 cal[]에는 평일만 넣으니까
                 
    #     d=d+datetime.timedelta(days=1)
    STOCK_LIST=[]
   # print(len(df.index))
   # print(len(dat))
    for i in range(len(dat)):
        
        stockInfo = [str(indexList[i]),dat[i]]
        STOCK_LIST.append(stockInfo)
        print(stockInfo)
        df = pd.DataFrame(STOCK_LIST, columns=('기간','종가'))
        js = df.to_json(orient='columns').encode().decode('unicode-escape')

    return js

prac()