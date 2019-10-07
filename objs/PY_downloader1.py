# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:27:35 2018

@author: kuifenhu
"""

from iexfinance.stocks import get_historical_data
from datetime import datetime, timedelta
from scipy import io as sio 
from time import time
def get_ticker_update(symbs,ndays):
# start = datetime(2013,11, 13)
# end = datetime(2017, 5, 24)
 start = datetime.today() - timedelta(days=ndays)
 end=datetime.today()
 result=[]
 n=0
 k=0
 failed=[]
 t0=time()
 CRED = '\033[91m'
 CEND = '\033[0m'
 for symb in symbs:
   try:
         df = get_historical_data(symb, start=start, end=end, output_format='pandas')     
         #df.reset_index(level=0,inplace=True)
         df1={}
         df1['data']=df.to_dict('list')
         df1['t']=df.index.tolist()
         df1['symbol']=symb
         result.append(df1)
         n=n+1
         print('TK'+str(n) +' :: '+symb+' loaded sucessfully')
   except:
         df1={}
         df1['data']=[]
         df1['t']=[]
         df1['symbol']=symb
         failed.append(symb)
         n=n+1
         k=k+1
         print(CRED +'TK'+str(n) +' :: '+symb + ' download failed','red'+CEND)
         continue
       
 sio.savemat('result.mat',{'tsPY':result})
 print('All done Total time '+str(int(time()-t0))+' Seconds') 
 print('Total ticker tried: '+str(n) ) 
 print('Sucessfully loaded: '+str(n-k) )
 print('Failed loaded: '+str(k) )
 print(*failed,sep=',')
 return(result)
ts=get_ticker_update('C',100)