# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:32:50 2018

@author: kuifenhu
"""
import os
os.environ["IEX_TOKEN"]="sk_181a16b9521c450b9f6ba7213cc4622a"
os.environ["IEX_OUTPUT_FORMAT"]="pandas"


from ControllerObj import ControllerObj
#
##%% Process symb
#
#s=SymbObj()
##s.loadsymb()
##s.loadfromfile()
#s.symb=['A','KEYS','COST','FTR','LTC','NHI','WELL','HD','SNH','CHCT','GEO','AAPL','AVGO','GOOG']
#s.symb=['BBY','NVDA','TSN','AAP','GE']
##s.symb = ['E', 'TOT', 'HON', 'OXY', 'BP', 'CVX', 'COP', 'HES', 'HFC', 'PSX']
##%% Process ticker download
#s.symb=['SNH']
#d = DownloaderObj(s)
#d.ndays=500
#d.period=1
#d.Download_ts()
##d.Download_keynum()
##d.Download_finviz()
##d.Download_pulse()
##d.peers('AAPL')
#
##%% Gui Main frame
#g=GuiObj(d)
#g.chart_ohlc()
##g.chart_keys()
#
##%% process TA
#ta=TaObj(d)
#ta.tp=14
#ta.inputdata=d.ts_result[g.ind]


# control panel. attached to GUI main frame
Ctr=ControllerObj()
Ctr.window.mainloop()

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

