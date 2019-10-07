# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:49:39 2019

@author: kuifenhu
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:51:09 2019

@author: kuifenhu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:27:35 2018

@author: kuifenhu
"""

from yahoo_historical import Fetcher
from datetime import datetime, timedelta
from scipy import io as sio 
from time import time
def get_ticker_update(symbs,ndays):
# start = datetime(2013,11, 13)
# end = datetime(2017, 5, 24)
 start = datetime.today() - timedelta(days=ndays)
 start1=[int(start.strftime('%Y')),int(start.strftime('%m')),int(start.strftime('%d'))]
 end=datetime.today()
 end1=[int(end.strftime('%Y')),int(end.strftime('%m')),int(end.strftime('%d'))]
 result=[]
 n=0
 k=0
 failed=[]
 t0=time()
 CRED = '\033[91m'
 CEND = '\033[0m'
 i=0
 for symb in symbs:
   try:  
         i=i+1
         if i>=200:
            i=0
            time.sleep(60)
        
         data=Fetcher(symb,start1,end1)
         df = data.getHistorical()   
         #df.reset_index(level=0,inplace=True)
         df1={}
         df['Adj_Close']=df['Adj Close']
         del df['Adj Close']
         df1['data']=df.to_dict('list')
         #df1['t']=df.index.tolist()
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
ts=get_ticker_update(['C','A'],100)