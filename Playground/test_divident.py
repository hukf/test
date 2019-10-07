# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:12:25 2018

@author: kuifenhu
"""
symbol=''
url=r'https://www.nasdaq.com/symbol/{}/dividend-history'.format(symbol.lower())
html = u.request.urlopen(url).read()
soup = bs(html, 'lxml')
#           # Change the text below to get a diff metric
#          self.result={}
#           k=0
#           for i in self.name:
#             try:   
#                   pb =  soup.find(text = i)
#                   tmp1= pb.find_next(class_='snapshot-td2').te
data = []
table = soup.find('table', attrs={'id':'quotes_content_left_dividendhistoryGrid'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
    
  
    
    
import numpy as np
    
url=r'https://www.finviz.com'
html = u.request.urlopen(url).read()
soup = bs(html, 'lxml')
result=[]

table = soup.find_all('table', attrs={'class':'t-home-table'})
#table_body = table.find('tbody')
for i in np.arange(len(table)):
    data = []    
    rows = table[i].find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
    result.append(data)