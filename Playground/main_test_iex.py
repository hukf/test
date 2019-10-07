# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:44:24 2018

@author: kuifenhu
"""

from iexfinance import Stock
from iexfinance import get_historical_data
import datetime
import matplotlib.pyplot as plt
from main_test import load_symbols
from iexfinance import get_market_tops
from iexfinance import get_stats_intraday
from iexfinance import *
import pandas as pd
def replace_none_with_empty_str(some_list):
    newlist=[]
    for some_dict in some_list:
       some_dict={ k: (pd.np.nan if v is None else v) for k, v in some_dict.items() }
       newlist.append(some_dict)
    return(newlist)
df={}
df['gainers']=replace_none_with_empty_str(get_market_gainers())
df['losers']=replace_none_with_empty_str(get_market_losers())
df['most_active']=replace_none_with_empty_str(get_market_most_active())
df['IEX_Volume']=replace_none_with_empty_str(get_market_iex_volume())
df['IEX_Percent']=replace_none_with_empty_str(get_market_iex_percent())

import datetime
#https://stackoverflow.com/questions/49710963/converting-13-digit-unixtime-in-ms-to-timestamp-in-python
timestamp = "1523126888080"
your_dt = datetime.datetime.fromtimestamp(int(timestamp)/1000)  # using the local timezone
print(your_dt.strftime("%Y-%m-%d %H:%M:%S")) 



io.savemat('test.mat',{'struct':df})

[symbol,symbol500]=load_symbols()

#Stocks

#tsla = Stock(symbol500.ix[[1,2],'Symbol'].values.T.tolist(),output_format='pandas')
#tsla = Stock(symbol500.iloc[0:1,0].values.T.tolist(),output_format='pandas')
allkeys={}
tsla = Stock('TSLA',output_format='pandas')
ohlc=tsla.get_ohlc()
ohlc.fillna(value=pd.np.nan, inplace=True)
quote=tsla.get_quote()
quote.fillna(value=pd.np.nan, inplace=True)
keys=tsla.get_key_stats()
keys.fillna(value=pd.np.nan, inplace=True)
financial=tsla.get_financials()
financial.fillna(value=pd.np.nan, inplace=True)
chart=tsla.get_chart()

allkeys['ohlc']=ohlc.to_dict()
allkeys['quote']=quote.to_dict()
allkeys['keys']=keys.to_dict()
allkeys['financial']=financial.to_dict()
allkeys['chart']=chart
io.savemat('result.mat',{'tsPY':allkeys})


# Historical Data

start = datetime(2013,11, 13)
#end = datetime(2017, 5, 24)
end=datetime.today()
df = get_historical_data('MMM', start=start, end=end, output_format='pandas')
df['date']=df.index
#df.drop(['date'],axis=1)
df.reset_index(level=0,inplace=True)
scipy.io.savemat('test.mat',{'struct':df.to_dict('list')})

#IES Market Data
a=get_market_tops('TSLA', output_format='pandas')
get_market_last()
get_market_deep()
get_market_book()
# IEX stats
get_stats_intraday()
get_stats_recent()[0]
get_stats_records()
get_stats_daily(last=3)
get_stats_monthly(start=datetime(2017, 2, 9), end=datetime(2017, 5, 24))[0]


b=get_stats_intraday('TSLA')

tsla = Stock(['TSLA','AAPL'],output_format='pandas')
tsla.get_open()
tsla.get_price()



df = get_historical_data("AAPL", start=start, end=end, output_format='pandas')
df.head()
df.tail()


df.plot()
plt.show()