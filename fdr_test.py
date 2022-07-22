
from datetime import date, datetime
from operator import index
import FinanceDataReader as fdr
import datetime
import pandas as pd

# 삼성전자(005930)
def prac():
    global d
    d = date(2022, 1, 11)
    dat =[]
    df = fdr.DataReader('005930', d.isoformat())

    
    
    dat=df['Close'].tolist()


    indexList= df.index.strftime("%Y-%m-%d").tolist()

   
    STOCK_LIST=[]
    
    for i in range(len(dat)):       
        stockInfo = [str(indexList[i]),dat[i]]
        STOCK_LIST.append(stockInfo)
        df = pd.DataFrame(STOCK_LIST, columns=('기간','종가'))
        js = df.to_json(orient='columns').encode().decode('unicode-escape')

    return js

prac()