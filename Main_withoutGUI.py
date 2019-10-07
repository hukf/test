# -*- coding: utf-8 -*-
#import tkinter as tk
#from tkinter import ttk
#from tkinter import *
#from objs.GuiObjFcn import GuiObjFcn
#from functools import partial
import matplotlib.pyplot as plt
import numpy as np
import pickle
from datetime import datetime
# call pop up file functions
import easygui
import dill
import pickle
import os,sys
os.sys.path.append(os.getcwd())
os.sys.path.append(os.path.join(os.getcwd(),'objs'))

# data frame
import pandas as pd
#%%
# self written Obj: symbol process
from objs.SymbObj import SymbObj 
# self written Obj: data download using iex and parser
from objs.DownloaderObj import DownloaderObj as stock
# self written Obj: plotting tools for OHLC plotting etc
#from objs.GuiObj import GuiObj as gui
# self written obj: to process Techincal indicator
from objs.TaObj import TaObj as ta
from objs.TradingAlgorithm import TradingAlgorithmObj as st
from openpyxl import load_workbook

# Initial some data holders
result={}
#************************************************
# Section 1, download finviz data
#1.1  Download holdings
s=SymbObj()
symb=['A','KEYS','COST','FTR','LTC','NHI','WELL','HD','SNH','CHCT','GEO','AAPL',
      'AVGO','GOOGL','AMZN','UNH','BIIB','ABBV','JNJ','KO','PEP','NVDA','FAST',
      'MO','PM','BP','RSD-A','JPM','WFC','COST','KR','ALL']
# 1.2.2 Download sp500 tickers
s.sector={'holding':symb}
s.loadfromfile()



sector=list(s.sector.keys())
for sec in sector:   
    s.symb=s.sector.get(sec)
    d = stock(s)
#    d.Download_finviz()
    d.Download_daychart(3)
#    d.xray()
#    d.summary.mean(axis=0)
#    d.summary.sort_values(by=['Total'], ascending =False)
    result.update({sec:d})
# 1.3 Save downloaded finviz data into database   Z 
PIK = './data/result'+datetime.now().strftime('%m_%d_%Y')+'.dat'
with open(PIK, "wb") as f:
    pickle.dump(result, f)

  
#*********************************************************************
#*********************************************************************
# Section 2 Data Anaysis    
# 2.1 Load the data into workspace. 
# Open data
PIK = './data/result'+datetime.now().strftime('%m_%d_%Y')+'.dat'
with open(PIK, "rb") as f:
    result=pickle.load(f)
    
TA=st(result)

# check the price change over one day. 
diff_result=TA.diff()
print(diff_result.sort_values(by=['Diff_Close']))
 
TA.tafa(5)
TA.newlow(5)
TA.newhigh(5)


  
#************************************************





d.ndays=500
d.period=1
d.Download_ts()
# data is downloaded to 
# [ohlc1v2v] into array d.ts_result
#d.ts[x].['data', 't', 'symbol']  as a structured data. 


d.Download_realtime()
# download realtime quote  to  d.realtime_result all keys are stored 


d.Download_quotetb()
# download quote table to  d.quotetb_result all keys are stored 



d.Download_pulse()
# download quote table to  d.pulse_result all keys are stored 

d.xray()
d.summary.mean(axis=0)
d.summary.sort_values(by=['Total'])



d.alert()
#d.peers('AAPL')
#
##%% Gui Main frame
#g=GuiObj(d)
#g.chart_ohlc()
##g.chart_keys()
#
##%% process TA
ta=TaObj()
ta.tp=14
ta.inputdata=d.ts_result[0]


# control panel. attached to GUI main frame
#Ctr=ControllerObj()
#Ctr.window.mainloop()

#p1.symb = p1.peers('LEA')
#p1.symb = ['LEA','FTR','LPX','KEYS']
#p1.symb = ['C','KEYS','AAPL']
#p1.symb = ['BP','JD','BABA','NWL']
#p1.symb = ['BP','JD','BABA','NWL']
#p1.symb = ['AMZN','AAPL','FB','NFLX']
#p1.symb = ['WMT','JD','KR','AMZN','COST','BB','BABA','JCP']
#p1.symb = ['BP','XOM','TOT','CVX','COP','RDS.A']


#p1.symb = ['E', 'TOT', 'HON', 'OXY', 'BP', 'CVX', 'COP', 'HES', 'HFC', 'PSX']
#p1.symb = ['E', 'TOT', 'HON', 'OXY', 'BP', 'CVX', 'COP', 'HES', 'HFC', 'PSX']

