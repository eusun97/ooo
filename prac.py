from datetime import date, datetime
import FinanceDataReader as fdr
import datetime
import pandas as pd

# 삼성전자(005930) 전체 (1996-11-05 ~ 현재)
# df = fdr.DataReader('005930')
# print(df)
def prac():
    global d
    d = date(2022, 7, 11)
    e = date(2022, 7, 8)
    #d=d+datetime.timedelta(days=2)
    print(d.isoformat()+"WWWW")
    global cal

    dat =[]
    df = fdr.DataReader('005930', d.isoformat(),"2022-07-15")
    print(df)

    dat=df['Close'].tolist()
    print(dat)
    cal=[]

    for num in range(len(dat)):
    #print(d.weekday())

        if(0 <= d.weekday() <=4):
            print(d.weekday())
            cal.append(d)

        d=d+datetime.timedelta(days=1)
    STOCK_LIST=[]
    print(len(cal))
    print(len(dat))

    for i in range(len(dat)):
        stockInfo = [str(cal[i]),dat[i]]
        STOCK_LIST.append(stockInfo)
        print(stockInfo)    
        df = pd.DataFrame(STOCK_LIST, columns=('기간','종가'))
        js = df.to_json(orient='columns').encode().decode('unicode-escape')
        
        return js
    prac()
