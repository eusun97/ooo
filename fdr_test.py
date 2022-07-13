from datetime import date
import FinanceDataReader as fdr

# 삼성전자(005930) 전체 (1996-11-05 ~ 현재)
# df = fdr.DataReader('005930')
# print(df)

d = date(2022, 7, 1)
print(d.isoformat())

df = fdr.DataReader('005930', d.isoformat(), '2022-07-12')
print(df)

print(df['Close'].tolist())