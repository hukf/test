# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:21:33 2018

@author: kuifenhu
"""

from iexfinance import get_historical_data
from iexfinance import *
from datetime import datetime, timedelta
from scipy import io as sio 
from time import time
from pandas import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from finvizObj import finvizObj
import pandas as pd
import easygui
import re
#%%
class data_holder(object):
    pass
class LoadPortfolioObj:
  def __init__(self):
    self.tk=data_holder()   
    self.tk.position=[]
    self.tk.symb=[]
    self.tk.quality=[]
    
  def loadfromfile(self):
    path= easygui.fileopenbox()
    df=pd.DataFrame.from_csv(path)
    
    for i in df['Cost Basis Per Share']:
        tmp=v2f(i)
         self.tk=data_holder()  
         self.tk.symb
    self.symb=[x.strip(' ') for x in df.index.tolist()]
    
def v2f(x):
    return float(re.sub('[$,]','',x.strip()))   