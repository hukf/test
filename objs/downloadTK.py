# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:51:37 2018

@author: kuifenhu
"""
from iexfinance import get_historical_data
from datetime import datetime, timedelta
from scipy import io 
from time import time
def get_ticker_update(symbs):
# start = datetime(2013,11, 13)
# end = datetime(2017, 5, 24)
 start = datetime.today() - timedelta(days=100)
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
       
 io.savemat('result.mat',{'tsPY':result})
 print('All done Total time '+str(int(time()-t0))+' Seconds') 
 print('Total ticker tried: '+str(n) ) 
 print('Sucessfully loaded: '+str(n-k) )
 print('Failed loaded: '+str(k) )
 print(*failed,sep=',')
 
 # else:
#     print(symb + 'download sucessfully')
 
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