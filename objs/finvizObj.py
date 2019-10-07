import pandas as pd
import urllib as u
from bs4 import BeautifulSoup as bs
import re
import numpy as np

"""
First visit www.Finviz.com and get the base url for the quote page.
example: http://finviz.com/quote.ashx?t=aapl

Then write a simple function to retrieve the desired ratio. 
In this example I'm grabbing Price-to-Book (mrq) ratio
"""
class finvizObj:
  def __init__(self):
      self.name=['Index'     ,
            'Market Cap'     ,
            'Income'         ,
            'Sales'          ,
            'Book/sh'        ,
            'Cash/sh'        ,
            'Dividend'       ,
            'Dividend %'     ,
            'Employees'      ,
            'Optionable'     ,
            'Shortable'      ,
            'Recom'          ,
            'P/E'            ,
            'Forward P/E'    ,
            'PEG'            ,
            'P/S'            ,
            'P/B'            ,
            'P/C'            ,
            'P/FCF'          ,
            'Quick Ratio'    ,
            'Current Ratio'  ,
            'Debt/Eq'        ,
            'LT Debt/Eq'     ,
            'SMA20'          ,
            'EPS (ttm)'      ,
            'EPS next Y'     ,
            'EPS next Q'     ,
            'EPS this Y'     ,
            'EPS next Y'     ,
            'EPS next 5Y'    ,
            'EPS past 5Y'    ,
            'Sales past 5Y'  ,
            'Sales Q/Q'      ,
            'EPS Q/Q'        ,
            'Earnings'       ,
            'SMA50'          ,
            'Insider Own'    ,
            'Insider Trans'  ,
            'Inst Own'       ,
            'Inst Trans'     ,
            'ROA'            ,
            'ROE'            ,
            'ROI'            ,
            'Gross Margin'   ,
            'Oper. Margin'   ,
            'Profit Margin'  ,
            'Payout'         ,
            'SMA200'         ,
            'Shs Outstand'   ,
            'Shs Float'      ,
            'Short Float'    ,
            'Short Ratio'    ,
            'Target Price'   ,
            '52W Range'      ,
            '52W High'       ,
            '52W Low'        ,
            'RSI (14)'       ,
            'Rel Volume'     ,
            'Avg Volume'     ,
            'Volume'         ,
            'Perf Week'      ,
            'Perf Month'     ,
            'Perf Quarter'   ,
            'Perf Half Y'    ,
            'Perf Year'      ,
            'Perf YTD'       ,
            'Beta'           ,
            'ATR'            ,
            'Volatility'     ,
            'Prev Close'     ,
            'Price'          ,
            'Change'         ,
            ]
#%%
  def get_dividend(self,symbol):
      
        url=r'https://www.nasdaq.com/symbol/{}/dividend-history'.format(symbol.lower())
        html = u.request.urlopen(url).read()
        soup = bs(html, 'lxml')
        self.dividend_result = []
        try: 
            table = soup.find('table', attrs={'id':'quotes_content_left_dividendhistoryGrid'})
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                self.dividend_result.append([ele for ele in cols if ele])
        except:
            print('Dividend Download Error, No data is availbe')
            self.dividend_result=[0]
        return(self.dividend_result)# Get rid of empty values
#%%
  def get_pulse(self):
        url=r'https://www.finviz.com'
        html = u.request.urlopen(url).read()
        soup = bs(html, 'lxml')
        self.pulse_result=[]
        
        table = soup.find_all('table', attrs={'class':'t-home-table'})
        #table_body = table.find('tbody')
        for i in np.arange(len(table)):
            data = []    
            rows = table[i].find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele]) # Get rid of empty values
            self.pulse_result.append(data)
#%%
  def get_keys(self,symbol):
    
       try:
           url=r'http://finviz.com/quote.ashx?t={}'.format(symbol.lower())
           html = u.request.urlopen(url).read()
           soup = bs(html, 'lxml')
           # Change the text below to get a diff metric
           self.result={}
           k=0
           for i in self.name:
             try:   
                   pb =  soup.find(text = i)
                   tmp1= pb.find_next(class_='snapshot-td2').text
#                   print(tmp1)
                   if k in [0,9,10,34,68,53]:
                       pb_=tmp1
                   elif k in [1,2,3,48,49,58]:
                       pb_=x2f(tmp1)
                   elif k in [7,23,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,50,54,55,60,61,62,63,64,65,71]:
                       pb_=p2f(tmp1)
                   elif k in [59] :
                       pb_=v2f(tmp1)
                   else:
                       if tmp1.strip() == '-':
                           tmp1='0'
                       pb_=float(tmp1)
                    
                   self.result[i.replace(' ','')]=pb_
#                   print( '{} {} = {}'.format(symbol,i, str(pb_) ))
                   k=k+1
             except Exception as e:
                   print(i+'error in '+tmp1 )  
           return(self.result)
           
       except Exception as e:
           print(e)

def p2f(x):
    if x.strip() == '-':
      x='0%'
    return float(x.strip('%'))/100    
def v2f(x):
    if x.strip() == '-':
      x='0,'
    return float(re.sub(',','',x))   
def x2f(x):
    if x.strip() == '-':
      x='0'
    num_replace = {'B' : 1000000000, 'M' : 1000000,'K':1000}
    mult = 1.0
    while x[-1] in num_replace:
        mult *= num_replace[x[-1]]
        x = x[:-1]
    return float(x) * mult 
  
"""
#Construct a pandas series whose index is the list/array
#of stock symbols of interest.
#
#Run a loop assigning the function output to the series
"""
###stock_list = ['XOM']
#a=finvizObj()
###for sym in stock_list:
#b=a.get_keys('KEYS')
#b=a.get_dividend('KEYS')
#b=a.get_pulse()
