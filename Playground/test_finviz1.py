# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:03:35 2018

@author: kuifenhu
"""

import pandas as pd
import urllib as u
from bs4 import BeautifulSoup as bs

"""
First visit www.Finviz.com and get the base url for the quote page.
example: http://finviz.com/quote.ashx?t=aapl

Then write a simple function to retrieve the desired ratio. 
In this example I'm grabbing Price-to-Book (mrq) ratio
"""

def get_price2book( symbol ):
	try:
    	url = r'http://finviz.com/quote.ashx?t={}'\
        				.format(symbol.lower())
        html = u.request.urlopen(url).read()
        soup = bs(html, 'lxml')
        # Change the text below to get a diff metric
        pb =  soup.find(text = r'P/B')
        pb_ = pb.find_next(class_='snapshot-td2').text
        print( '{} price to book = {}'.format(symbol, pb_) )
        return pb_
    except Exception as e:
        print(e)
        
"""
Construct a pandas series whose index is the list/array
of stock symbols of interest.

Run a loop assigning the function output to the series
"""
stock_list = ['XOM','AMZN','AAPL','SWKS']
p2b_series = pd.Series( index=stock_list )

for sym in stock_list:
	p2b_series[sym] = get_price2book(sym)