# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:45:07 2018

@author: kuifenhu
"""
import re
import pandas as pd
a=[
[],
['SPY181203C00200000',
 '2018-11-23 12:59PM EST',
 '200.00',
 '63.40',
 '74.08',
 '74.56',
 '0.00',
 '-',
 '5',
 '7',
 '126.17%'],
 ['SPY181203C00240000',
 '2018-11-26 9:33AM EST',
 '240.00',
 '25.92',
 '34.12',
 '34.59',
 '0.00',
 '-1.2%',
 '1',
 '17',
 '61.62%']]
header=['Contract','Last_Trade_Date','Strike','Price',	'Bid'	,'Ask'	,'Change', 'Change%'	,'Volume','OpenInterests','Volatility']

a.pop(0)
df=pd.DataFrame(a,columns=header)
df['Strike']=list(map(lambda x :float(re.sub('-', '0', x)), df['Strike']))
df['Price']=list(map(lambda x :float(re.sub('-', '0', x)), df['Price']))
df['Bid']=list(map(lambda x :float(re.sub('-', '0', x)), df['Bid']))

df['Ask']=list(map(lambda x :float(re.sub('-', '0', x)), df['Ask']))
df['Change']=list(map(lambda x :float(re.sub('', '', x)), df['Change']))
df['Change%']=list(map(lambda x :float(re.sub('-', '0', x)) if len(x)==1 else float(re.sub('%', '', x))*0.01 , df['Change%']))
df['Volume']=list(map(lambda x :float(re.sub(',', '', x)), df['Volume']))
df['OpenInterests']=list(map(lambda x :float(re.sub(',', '', x)), df['OpenInterests']))
df['Volatility']=list(map(lambda x :float(re.sub('%', '', x))*0.01, df['Volatility']))

