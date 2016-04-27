import random
import numpy as np
import pandas as pd
import pandas.io.data as web
import datetime

d0 = datetime.date.today() #d0 是今天

d0 = d0 - datetime.timedelta(days = 1)   #如果以後要換日期，就用這個

start = d0
"""
http://www.jpx.co.jp/markets/statistics-equities/misc/01.html
這個是東証的檔,裡面應該有所有的可交易代號
http://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls
這個檔是可以下載的，不過不知道前面的東西會不會變
"""
#toyota_nyse = web.DataReader('TM', 'yahoo', start=start)

def get_quote_yahoojp(code, start=None, end=None, interval='d'):
    base = 'http://info.finance.yahoo.co.jp/history/?code={0}.T&{1}&{2}&tm={3}&p={4}'
    start, end = web._sanitize_dates(start, end)
    start = 'sy={0}&sm={1}&sd={2}'.format(start.year, start.month, start.day)
    end = 'ey={0}&em={1}&ed={2}'.format(end.year, end.month, end.day)
    p = 1
    results = []

    if interval not in ['d', 'w', 'm', 'v']:
        raise ValueError("Invalid interval: valid values are 'd', 'w', 'm' and 'v'")

    while True:
        url = base.format(code, start, end, interval, p)
        tables = pd.read_html(url, header=0)
        if len(tables) < 2 or len(tables[1]) == 0:
            break
        results.append(tables[1])
        p += 1
    result = pd.concat(results, ignore_index=True)

    result.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    if interval == 'm':
        result['Date'] = pd.to_datetime(result['Date'], format='%Y年%m月')
    else:
        result['Date'] = pd.to_datetime(result['Date'], format='%Y年%m月%d日')
    result = result.set_index('Date')
    result = result.sort_index()
    return result

#def print_quote

darts = [i for i in range(1000,10000)]

random.shuffle(darts)

dartsAftShuffle = []

while len(dartsAftShuffle) <5:
    try:
        null_tse = get_quote_yahoojp(darts[0], start=start)
        null_tse.head()
        dartsAftShuffle.append(null_tse.head())
        del darts[0]
    except ValueError as Verr:    
        del darts[0]

print(dartsAftShuffle)
print(darts[:5])
