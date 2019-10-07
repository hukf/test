# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:56:39 2018

@author: kuifenhu
"""
from iexfinance import get_market_book
 
a=get_market_book("LPX")
#%%
a=get_market_deep("KEYS")
b=a['trades']
for c in b:
    print(datetime.datetime.fromtimestamp(int(c['timestamp'])/1000).strftime('%Y-%m-%d %H:%M:%S')
           +' Price::$'+ str(c['price']) +', Size '+str(c['size']) )
#%%
import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime
a=p1.ts_result[0]['t']
df=pd.DataFrame.from_dict(p1.ts_result[0]['data'])
dt=pd.DataFrame.from_dict({'Date':a})
trace = go.Candlestick(x=dt.Date,
                       open=df.open,
                       high=df.high,
                       low=df.low,
                       close=df.close)
data = [trace]
py.iplot(data, filename='simple_candlestick')

