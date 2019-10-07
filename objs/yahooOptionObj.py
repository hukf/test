import pandas as pd
import urllib as u
from bs4 import BeautifulSoup as bs
import re
import numpy as np
from datetime import datetime
import time
import pytz

#from datetime import datetime
#from dateutil.relativedelta import relativedelta
#
#print 'Today: ',datetime.now().strftime('%d/%m/%Y %H:%M:%S') 

#from datetime import datetime
#ts = int("1284101485")
#convert string to UTC timestamp
#t=datetime(2018,11,27,17,0,0)
#tmp=time.mktime(t.timetuple())

# convert time utc to string
## if you encounter a "year is out of range" error the timestamp
## may be in milliseconds, try `ts /= 1000` in that case
#print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
#print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
#pirnt in native C format.
#print(datetime.utcfromtimestamp(ts).ctime())
#print in ISO format
#print(datetime.utcfromtimestamp(ts).isoformat())

## apply timezone
#d=datetime(2018,11,28,0,0,0)
#d_aware = timezone.localize(d)
#d_aware.astimezone(pytz.timezone("UTC")).isoformat()


"""
First visit www.Finviz.com and get the base url for the quote page.
example: http://finviz.com/quote.ashx?t=aapl

Then write a simple function to retrieve the desired ratio. 
In this example I'm grabbing Price-to-Book (mrq) ratio
"""
class yahooOptionObj:
  def __init__(self):
      self.option_result=[]
      self.option_call=[]
      self.option_put=[]



#%%
  def get_option(self,symb,t):
#      https://finance.yahoo.com/quote/AAPL/options?p=AAPL&.tsrc=fin-srch&date=1546560000
#      https://finance.yahoo.com/quote/SPY/options?p=SPY&.tsrc=fin-srch&date=1543968000
        tmp=str(int(time.mktime(t.timetuple())))
        url=r'https://finance.yahoo.com/quote/'+symb.strip().upper()+'/options?p='+symb.strip().upper()+'&date='+tmp+'&.tsrc=fin-srch'
        html = u.request.urlopen(url).read()
        soup = bs(html, 'lxml')

        
        table = soup.find_all('table', attrs={'class':'calls table-bordered W(100%) Pos(r) Bd(0) Pt(0) list-options'})
        #table_body = table.find('tbody')
        for i in np.arange(len(table)):
            data = []    
            rows = table[i].find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele]) # Get rid of empty values
            self.option_call.append(data)
            
        table = soup.find_all('table', attrs={'class':'puts table-bordered W(100%) Pos(r) list-options'})
        #table_body = table.find('tbody')puts table-bordered W(100%) Pos(r) list-options
        for i in np.arange(len(table)):
            data = []    
            rows = table[i].find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele]) # Get rid of empty values
            self.option_put.append(data)
    
    
        for i in self.option_call[0]:
            print(i)
        for i in self.option_put[0]:
            print(i)
            
            

def p2f(x):
  
"""
#Construct a pandas series whose index is the list/array
#of stock symbols of interest.
#
#Run a loop assigning the function output to the series
"""
##stock_list = ['XOM']
a=yahooOptionObj()
t=datetime(2018,12,2,17,0,0)
a.get_option('SPY',t)

