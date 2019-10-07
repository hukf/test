# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:44:01 2018

@author: kuifenhu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:45:07 2018

@author: kuifenhu
"""
import re
import pandas as pd
import easygui
path= easygui.fileopenbox()
df=pd.DataFrame.from_csv(path)
d = dict(zip(df['Symbol'][df['Cost Basis Per Share']!='n/a'],df['Cost Basis Per Share'][df['Cost Basis Per Share']!='n/a']))
d1 = {k: float(re.sub('[$,]','',v)) for k, v in d.items()}
d2 = {key:val for key, val in d1.items() if val != 0}



self.symb=[x.strip(' ') for x in df.index.tolist()]


df['Strike']=list(map(lambda x :float(re.sub('-', '0', x)), df['Strike']))
df['Price']=list(map(lambda x :float(re.sub('-', '0', x)), df['Price']))
df['Bid']=list(map(lambda x :float(re.sub('-', '0', x)), df['Bid']))

df['Ask']=list(map(lambda x :float(re.sub('-', '0', x)), df['Ask']))
df['Change']=list(map(lambda x :float(re.sub('', '', x)), df['Change']))
df['Change%']=list(map(lambda x :float(re.sub('-', '0', x)) if len(x)==1 else float(re.sub('%', '', x))*0.01 , df['Change%']))
df['Volume']=list(map(lambda x :float(re.sub(',', '', x)), df['Volume']))
df['OpenInterests']=list(map(lambda x :float(re.sub(',', '', x)), df['OpenInterests']))
df['Volatility']=list(map(lambda x :float(re.sub('%', '', x))*0.01, df['Volatility']))
