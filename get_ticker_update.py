# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:51:37 2018

@author: kuifenhu
"""
from iexfinance.stocks import get_historical_data
from datetime import datetime, timedelta
import scipy  

def get_ticker_update(symb):
# start = datetime(2013,11, 13)
# end = datetime(2017, 5, 24)
 start = datetime.today() - timedelta(days=100)
 end=datetime.today()
 df = get_historical_data(symb, start=start, end=end, output_format='pandas')     
 df.reset_index(level=0,inplace=True)
 scipy.io.savemat('test.mat',{'struct':df.to_dict('list')})
 
# df1=df.to_dict('list')  
# scipy.io.savemat('test.mat',{'struct':df.to_dict('list')})
# df2={} 
# df2['Symbol']='MMM'
# df2['data']=df1
#
#
# 
# df3={} 
# df3['Symbol']='MMM'
# df3['data']=df1
# df4=[df2,df3]
# scipy.io.savemat('test.mat',{'ts':df4})