# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:45:31 2018

@author: kuifenhu
"""

from iexfinance import get_historical_data
from datetime import datetime, timedelta
from scipy import io 

def get_keys_update(symb):
# start = datetime(2013,11, 13)
# end = datetime(2017, 5, 24)
 start = datetime.today() - timedelta(days=100)
 end=datetime.today()
 result=[]
 try:
     for symb1 in symb: 
         df = get_historical_data(symb1, start=start, end=end, output_format='pandas')     
         #df.reset_index(level=0,inplace=True)
         df1={}
         df1['data']=df.to_dict('list')
         df1['t']=df.index.tolist()
         df1['symbol']=symb
     result.append(df1)
     io.savemat('result.mat',{'tsPY':result})
     print('download sucessful')
 except:
     df1={}
     df1['data']=[]
     df1['t']=[]
     df1['symbol']=symb
     print(symb + 'download failed')