#%%-*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:34:25 2018

@author: kuifenhu
"""

# this GUI is developed from the origin below
# it use tkinter group function 

#http://interactivepython.org/runestone/static/CS152f17/GUIandEventDrivenProgramming/05_widget_grouping.html
import tkinter as tk
from tkinter import ttk
from tkinter import *
from objs.GuiObjFcn import GuiObjFcn
from functools import partial
import matplotlib.pyplot as plt
import numpy as np
# call pop up file functions
import easygui
import dill
# data frame
import pandas as pd
#%%
# self written Obj: symbol process
from objs.SymbObj import SymbObj
# self written Obj: data download using iex and parser
from objs.DownloaderObj import DownloaderObj
# self written Obj: plotting tools for OHLC plotting etc
from objs.GuiObj import GuiObj
# self written obj: to process Techincal indicator
from objs.TaObj import TaObj
#%%

class entry_holder(object):
    pass

       
class ControllerObj():
    def __init__(self):
        # from tk Grouping Examples
        #Create the consel window
        self.window = tk.Tk()
        self.window.title("Main Control Consel")
        self.lines=[]
        
        
        #instaniate symbol obj
        self.s=SymbObj()
        #set defualt symb ticker
#       s.symb=['A','KEYS','COST','FTR','LTC','NHI','WELL','HD','SNH','CHCT','GEO','AAPL','AVGO','GOOG']
#       s.symb=['BBY','NVDA','TSN','AAP','GE']
        self.s.symb=['AAPL']
        
        #insitaniate data obj
        self.d=DownloaderObj(self.s)
        # config data obj
        # select the range of time series strting from today back ndays
        self.d.ndays=100
        #select the frequency by default 1 day
        self.d.period=1
        # execute download action
        self.d.Download_ts()
        
        
        # control panel. attached to GUI main frame
        #instaniate object TA given the data obj d. 
        self.ta=TaObj(self.d)
        #config ta obj: time period
        self.ta.tp=14
        # config ta obj: input data
        self.ta.inputdata=self.d.ts_result[0]
    
        #instaniate object GUI, the main trace plotting window, give the data obj d. 
        self.g=GuiObj(self.d)
        
        #populate the rest of widgets on control consel panel
        self.create_widgets()

#%% Define the action associated with each button, from cmd of TA
    # if cmd output format is Pattern
    def showPattern(self,str1):
      plt.sca(self.g.ax)
      try:
          plt.plot(self.ta.t[self.ta.integer==100],self.ta.close[self.ta.integer==100],color='red', marker='*',markersize=15,linestyle="None",label=str1+'pos')
          plt.plot(self.ta.t[self.ta.integer==-100],self.ta.close[self.ta.integer==-100],color='blue', marker='*',markersize=15,linestyle="None",label=str1+'neg')
          self.g.fig_ohlc.canvas.draw()
          self.g.fig_ohlc.canvas.flush_events() 
      except:
              pass
    # if cmd output format is Indicator
    def showIndicator(self,str1):
          plt.sca(self.g.ax1)
          plt.cla()
          N=len(self.ta.output)
          if N>=5:
             l1,=plt.plot(self.ta.t,self.ta.output,label=str1)
             self.lines.append(l1) 
          else: 
              for i in np.arange(N):
                 l1,=plt.plot(self.ta.t,self.ta.output[i],label=str1)
                 self.lines.append(l1)
    #            exec('self.'+str1+'.append(l1)')
          self.g.fig_ohlc.canvas.draw()
          self.g.fig_ohlc.canvas.flush_events() 
          
    #if cmd output format is Overlay
    def showOverlay(self,str1)    :
          plt.sca(self.g.ax)
          N=len(self.ta.output)
          if N>=5:
             l1,=plt.plot(self.ta.t,self.ta.output,label=str1)
             self.lines.append(l1) 
          else: 
              for i in np.arange(N):
                  l1,=plt.plot(self.ta.t,self.ta.output[i],label=str1)
                  self.lines.append(l1)
#          exec('self.'+str1+'.append(l1)')
          self.g.fig_ohlc.canvas.draw()
          self.g.fig_ohlc.canvas.flush_events() 
          
#%% Define the action associated with each button -- from cmd of action
    def showCustom(self,str1):
        if str1 is 'Cursor':
            if self.g.cursor.visible==True:
               self.g.cursor.visible=False
            else:
               self.g.cursor.visible=True
        elif str1 is 'LoadHolding':
            # open exel file from fidelity. parse the symbol and cost basis.
            path= easygui.fileopenbox()
            df=pd.DataFrame.from_csv(path)
            d = dict(zip(df['Symbol'][df['Cost Basis Per Share']!='n/a'],df['Cost Basis Per Share'][df['Cost Basis Per Share']!='n/a']))
            d1 = {k: float(re.sub('[$,]','',v)) for k, v in d.items()}
            d2 = {key:val for key, val in d1.items() if val != 0}
            self.d.symb=list(d2.keys())
            self.d.holdings=d2
            self.d.Download_ts()
            self.treeview.update(self.d.symb)
        
        elif str1 is 'AddTicker':
             tmp=self.entrys.addsymb.get().strip().upper().split(',')
             self.d.symb=self.d.symb+tmp
             self.d.Download_ts()
             self.treeview.update(self.d.symb)
             
        elif str1 is 'LoadTicker':
             
             path=self.s.loadfromfile()
             self.entrys.loadsymb.insert(0,path)
             self.d = DownloaderObj(self.s)
             self.treeview.update(self.d.symb)
        
        elif str1 is 'Load_ts':
             if self.entrys.pd.get().strip() is '':
                 self.d.period=1
             else:
                 self.d.period=float(self.entrys.pd.get().strip())
       
             if self.entrys.ndays.get().strip() is '':
                 self.d.ndays=500
             else:
                 self.d.ndays=float(self.entrys.ndays.get().strip())
             self.d.Download_ts()
             self.g=GuiObj(self.d)
             
        elif str1 is 'Load_key':
             self.d.Download_keynum()
        elif str1 is 'Load_pulse':
            self.d.Download_pulse()
        elif str1 is 'Load_finviz':
            self.d.Download_finviz()
        elif str1 is 'TA':
             pass
        
        elif str1 is 'OHLC':
            self.g.chart_ohlc()
        elif str1 is 'KeysChart':
            self.g.chart_keys()
            
            
        elif str1 is 'Save':
            path= easygui.filesavebox()
            with open(path, 'wb') as f:
                dill.dump(self.d, f)
                dill.dump(self.ta, f)
        elif str1 is 'Load':
            path= easygui.fileopenbox()
            with open(path, 'rb') as f:
                     self.d = dill.load(f)
                     self.ta = dill.load(f)
     
             
    def remove(self):
          for i in np.arange(len(self.lines)):
             self.lines.pop(0).remove()
             
    def remove1(self,ax,para):
          plt.sca(ax)
          tmp=[]
          str1='tmp=self.'+para
          for i in np.arange(len(tmp)):
             tmp.pop(0).remove()
#%%
    def GuiObjFcn(self,str1):
        self.ta.calculate(str1)
        if str1 in list(self.Grp_custom.keys()):
            self.showCustom(str1)
        elif str1 in list(self.Grp_overlay.keys()) :
            self.showOverlay(str1)
        elif str1 in list(self.Grp_momentum.keys()) :
            self.showIndicator(str1)
        elif str1 in list(self.Grp_volum.keys()) :
            self.showIndicator(str1)
        elif str1 in list(self.Grp_cycle_ind.keys()) :
            self.showIndicator(str1)
        elif str1 in list(self.Grp_price_trans.keys()) :
            self.showIndicator(str1)
        elif str1 in list(self.Grp_volatility.keys()) :
            self.showOverlay(str1)
        elif str1 in list(self.Grp_pattern.keys()) :
            self.showPattern(str1)           
        elif str1 in list(self.Grp_stat.keys()) :
            self.showIndicator(str1)
        else:
            pass
#%%          
    def create_buttons(self, parent,bts):
        k=1
        m=1
        for i in bts:
            if k>=15:
                k=1
                m=m+1
            #str1="self.bt_"+i+" = ttk.Button(parent, text='"+i+"',command=lambda: partial(GuiObjFcn,'"+i+"'))"
            str1="self.bt_"+i+" = ttk.Button(parent, text='"+i+"',command= partial(self.GuiObjFcn,'"+i+"'))"
            #print(str1)
            exec(str1) 
            str1="self.bt_"+i+".grid(row="+str(k)+", column="+str(m)+")"
 #           print(str)
            exec(str1)
            k=k+1
    
#%% 
    def create_entry1(self,parent,row,column):
#         
#         setattr(self.entrys,name+'Val',StringVar())
##        exec(str1)
###       label=Label(parent, text=caption)
#         str1="self.entrys."+name+"=Entry(parent, text='14',textvariable=self.entrys."+name+"Val)"
#         exec(str1)
#         str1="self.entrys."+name+".grid(row=row,column=column)"
#         exec(str1)
          v=StringVar()
          entry=Entry(parent, text='14',textvariable=v)
          entry.grid(row=row,column=column)
          return entry
#%% 
    def create_label1(self,parent,caption,row,column):
         
         label=Label(parent, text=caption)
         label.grid(row=row,column=column)
         return label
              
#%% 
    def create_entrys(self, parent):
         
#        self.entry_content=[]
#        self.v0 = StringVar()
#        self.v1 = StringVar()
#        self.v2= StringVar()
#        self.v3 = StringVar()
#        
#        caption='TimePeriod 1:'
#        label=Label(parent, text=caption)
#        label.grid(row=1,column=1)
#        self.e1 = Entry(parent, text='14',textvariable=self.v0)
#        self.e1.grid(row=2,column=1)
#        self.entry_content.append((self.v0.get()))
#        
#        caption='TimePeriod 2:'
#        label=Label(parent, text=caption)
#        label.grid(row=3,column=1)
#        self.e2 = Entry(parent, text='14',textvariable=self.v1)
#        self.e2.grid(row=4,column=1)
#        self.entry_content.append((self.v1.get()))
#        
#        caption='TimePeriod 3:'
#        label=Label(parent, text=caption)
#        label.grid(row=5,column=1)
#        self.e3 = Entry(parent, text='14',textvariable=self.v2)
#        self.e3.grid(row=6,column=1)
#        self.entry_content.append((self.v2.get()))
#        
#        caption='Ticker'
#        label=Label(parent, text=caption)
#        label.grid(row=7,column=1)
#        self.e4 = Entry(parent, text='14',textvariable=self.v3)
#        self.e4.grid(row=8,column=1)
#        self.entry_content.append((self.v3.get()))
        
        pass
        
#%%        
    def create_widgets(self):
        self.entrys=entry_holder()
        self.labels=entry_holder()
        
      
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

#        # - - - - - - - - - - - - - - - - - - - - -
        # Frame
        frame_label = ttk.Label(self.window, text="Parameter Input")
        frame_label.grid(row=1, column=1, sticky=tk.W+ tk.N, pady=3)

        frame1 = ttk.Frame(self.window, relief=tk.RIDGE)
        frame1.grid(row=2, column=1, sticky=tk.E + tk.W + tk.N+tk.S, padx=30, pady=4)
        #Instanitate treeview obj on the left.
        self.treeview=AddTreeView(frame1,self.g)
        self.treeview.tree.pack(expand=True, fill='both')
        
        
        frame2 = ttk.Frame(self.window, relief=tk.RIDGE)
        frame2.grid(row=3, column=1, sticky=tk.E + tk.W + tk.N+tk.S, padx=30, pady=4)
     
        notebook_label = ttk.Label(self.window, text="Notebook")
        notebook_label.grid(row=1, column=2, sticky=tk.W, pady=3)

        notebookHolder = ttk.Notebook(self.window)
        notebookHolder.grid(row=2, column=2, sticky=tk.E + tk.W + tk.N + tk.S, padx=30, pady=4)

        # add tabs to notebook
        tab0 = tk.Frame(notebookHolder)
        tab1 = tk.Frame(notebookHolder)
        tab2 = tk.Frame(notebookHolder)
        tab3 = tk.Frame(notebookHolder)
        tab4 = tk.Frame(notebookHolder)
        tab5 = tk.Frame(notebookHolder)
        tab6 = tk.Frame(notebookHolder)
        tab7 = tk.Frame(notebookHolder)
        tab8 = tk.Frame(notebookHolder)
        
        notebookHolder.add(tab0, text="Custome", compound=tk.TOP)
        notebookHolder.add(tab1, text="Overlap ", compound=tk.TOP)
        notebookHolder.add(tab2, text="Momentum", compound=tk.TOP)
        notebookHolder.add(tab3, text="Volumn", compound=tk.TOP)
        notebookHolder.add(tab4, text="Cycle indicator", compound=tk.TOP)
        notebookHolder.add(tab5, text="Voltality", compound=tk.TOP)
        notebookHolder.add(tab6, text="Price Transformation", compound=tk.TOP)
        notebookHolder.add(tab7, text="Pattern Recognition", compound=tk.TOP)
        notebookHolder.add(tab8, text="Statistics", compound=tk.TOP)
        
        #define the buttons cmd
        self.Grp_custom={'Cursor':'Turn on off Cursor',
                         'LoadHolding':'Load holding from Fidelity',
                         'AddTicker':'Add new ticker',
                         'LoadTicker':'Load ticker from file',
                         'Load_ts':'Load TS',
                         'Load_key':'Load keys',                         
                         'Load_pulse':'Load pulse',
                         'Load_finviz':'Load finviz',
                         'TA':'Calculate TA',
                         'OHLC':'OHLC chart',
                         'KeysChart':'Chart for Keys',
                         'Save':'Save Class',
                         'Load':'Load Class',
                         'OHLC':'OHLC chart',
                         'reserved':'test'}
        self.Grp_overlay={'BBANDS'        :'Bollinger Bands                                ',
            'DEMA':'Double Exponential Moving Average              ',
            'EMA':'Exponential Moving Average                     ',
            'HT_TRENDLINE':'Hilbert Transform - Instantaneous Trendline    ',
            'KAMA':'Kaufman Adaptive Moving Average                ',
            'MA':'Moving average                                 ',
            'MAMA':'MESA Adaptive Moving Average                   ',
            'MAVP':'Moving average with variable period            ',
            'MIDPOINT':'MidPoint over period                           ',
            'MIDPRICE':'Midpoint Price over period                     ',
            'SAR':'Parabolic SAR                                  ',
            'SAREXT':'Parabolic SAR - Extended                       ',
            'SMA':'Simple Moving Average                          ',
            'T3':'Triple Exponential Moving Average (T3)         ',
            'TEMA':'Triple Exponential Moving Average              ',
            'TRIMA':'Triangular Moving Average                      ',
            'WMA':'Weighted Moving Average                        '}
        self.Grp_momentum={'ADX':      'Average Directional Movement Index',
            'ADXR':'AverageDirectionalMovementIndexRating',
            'APO':'AbsolutePriceOscillator',
            'AROON':'Aroon',
            'AROONOSC':'AroonOscillator',
            'BOP':'BalanceOfPower',
            'CCI':'CommodityChannelIndex',
            'CMO':'ChandeMomentumOscillator',
            'DX':'DirectionalMovementIndex',
            'MACD':'MovingAverageConvergence/Divergence',
            'MACDEXT':'MACDwithcontrollableMAtype',
            'MACDFIX':'MovingAverageConvergence/DivergenceFix12/26',
            'MFI':'MoneyFlowIndex',
            'MINUS_DI':'MinusDirectionalIndicator',
            'MINUS_DM':'MinusDirectionalMovement',
            'MOM':'Momentum',
            'PLUS_DI':'PlusDirectionalIndicator',
            'PLUS_DM':'PlusDirectionalMovement',
            'PPO':'PercentagePriceOscillator',
            'ROC':'Rateofchange:((price/prevPrice)-1)*100',
            'ROCP':'RateofchangePercentage:(price-prevPrice)/prevPrice',
            'ROCR':'Rateofchangeratio:(price/prevPrice)',
            'ROCR100':'Rateofchangeratio100scale:(price/prevPrice)*100',
            'RSI':'RelativeStrengthIndex',
            'STOCH':'Stochastic',
            'STOCHF':'StochasticFast',
            'STOCHRSI':'StochasticRelativeStrengthIndex',
            'TRIX':'1-dayRate-Of-Change(ROC)ofaTripleSmoothEMA',
            'ULTOSC':'UltimateOscillator',
            'WILLR':    'Williams%R'}
        self.Grp_volum={'AD':' Chaikin A/D Line',
            'ADOSC'                :'Chaikin A/D Oscillator',
            'OBV':                  'On Balance Volume'   }
        self.Grp_cycle_ind={'HT_DCPERIOD'          :'Hilbert Transform - Dominant Cycle Period ',
            'HT_DCPHASE'           :'Hilbert Transform - Dominant Cycle Phase  ',
            'HT_PHASOR'            :'Hilbert Transform - Phasor Components     ',
            'HT_SINE'              :'Hilbert Transform - SineWave              ',
            'HT_TRENDMODE'         :'Hilbert Transform - Trend vs Cycle Mode   ' }
        self.Grp_price_trans={'AVGPRICE':'Average Price        ',
            'MEDPRICE':'Median Price         ',
            'TYPPRICE':'Typical Price        ',
            'WCLPRICE':'Weighted Close Price '
                }
        self.Grp_volatility={'ATR':                  'Average True Range',
            'NATR':                ' Normalized Average True Range',
            'TRANGE':              'True Range'}
        self.Grp_pattern={ 'CDL2CROWS'          :'Two Crows                                                 ',
             'CDL3BLACKCROWS':'Three Black Crows                                         ',
             'CDL3INSIDE':'Three Inside Up/Down                                      ',
             'CDL3LINESTRIKE':'Three-Line Strike                                         ',
             'CDL3OUTSIDE':'Three Outside Up/Down                                     ',
             'CDL3STARSINSOUTH':'Three Stars In The South                                  ',
             'CDL3WHITESOLDIERS':'Three Advancing White Soldiers                            ',
             'CDLABANDONEDBABY':'Abandoned Baby                                            ',
             'CDLADVANCEBLOCK':'Advance Block                                             ',
             'CDLBELTHOLD':'Belt-hold                                                 ',
             'CDLBREAKAWAY':'Breakaway                                                 ',
             'CDLCLOSINGMARUBOZU':'Closing Marubozu                                          ',
             'CDLCONCEALBABYSWALL':'Concealing Baby Swallow                                   ',
             'CDLCOUNTERATTACK':'Counterattack                                             ',
             'CDLDARKCLOUDCOVER':'Dark Cloud Cover                                          ',
             'CDLDOJI':'Doji                                                      ',
             'CDLDOJISTAR':'Doji Star                                                 ',
             'CDLDRAGONFLYDOJI':'Dragonfly Doji                                            ',
             'CDLENGULFING':'Engulfing Pattern                                         ',
             'CDLEVENINGDOJISTAR':'Evening Doji Star                                         ',
             'CDLEVENINGSTAR':'Evening Star                                              ',
             'CDLGAPSIDESIDEWHITE':'Up/Down-gap side-by-side white lines                      ',
             'CDLGRAVESTONEDOJI':'Gravestone Doji                                           ',
             'CDLHAMMER':'Hammer                                                    ',
             'CDLHANGINGMAN':'Hanging Man                                               ',
             'CDLHARAMI':'Harami Pattern                                            ',
             'CDLHARAMICROSS':'Harami Cross Pattern                                      ',
             'CDLHIGHWAVE':'High-Wave Candle                                          ',
             'CDLHIKKAKE':'Hikkake Pattern                                           ',
             'CDLHIKKAKEMOD':'Modified Hikkake Pattern                                  ',
             'CDLHOMINGPIGEON':'Homing Pigeon                                             ',
             'CDLIDENTICAL3CROWS':'Identical Three Crows                                     ',
             'CDLINNECK':'In-Neck Pattern                                           ',
             'CDLINVERTEDHAMMER':'Inverted Hammer                                           ',
             'CDLKICKING':'Kicking                                                   ',
             'CDLKICKINGBYLENGTH':'Kicking - bull/bear determined by the longer marubozu     ',
             'CDLLADDERBOTTOM':'Ladder Bottom                                             ',
             'CDLLONGLEGGEDDOJI':'Long Legged Doji                                          ',
             'CDLLONGLINE':'Long Line Candle                                          ',
             'CDLMARUBOZU':'Marubozu                                                  ',
             'CDLMATCHINGLOW':'Matching Low                                              ',
             'CDLMATHOLD':'Mat Hold                                                  ',
             'CDLMORNINGDOJISTAR':'Morning Doji Star                                         ',
             'CDLMORNINGSTAR':'Morning Star                                              ',
             'CDLONNECK':'On-Neck Pattern                                           ',
             'CDLPIERCING':'Piercing Pattern                                          ',
             'CDLRICKSHAWMAN':'Rickshaw Man                                              ',
             'CDLRISEFALL3METHODS':'Rising/Falling Three Methods                              ',
             'CDLSEPARATINGLINES':'Separating Lines                                          ',
             'CDLSHOOTINGSTAR':'Shooting Star                                             ',
             'CDLSHORTLINE':'Short Line Candle                                         ',
             'CDLSPINNINGTOP':'Spinning Top                                              ',
             'CDLSTALLEDPATTERN':'Stalled Pattern                                           ',
             'CDLSTICKSANDWICH':'Stick Sandwich                                            ',
             'CDLTAKURI':'Takuri (Dragonfly Doji with very long lower shadow)       ',
             'CDLTASUKIGAP':'Tasuki Gap                                                ',
             'CDLTHRUSTING':'Thrusting Pattern                                         ',
             'CDLTRISTAR':'Tristar Pattern                                           ',
             'CDLUNIQUE3RIVER':'Unique 3 River                                            ',
             'CDLUPSIDEGAP2CROWS':'Upside Gap Two Crows                                      ',
             'CDLXSIDEGAP3METHODS':'Upside/Downside Gap Three Methods                         '}
        self.Grp_stat={'BETA'                 :'Beta                                   ',
            'CORREL'               :'Pearsons Correlation Coefficient (r)  ',
            'LINEARREG'            :'Linear Regression                      ',
            'LINEARREG_ANGLE'      :'Linear Regression Angle                ',
            'LINEARREG_INTERCEPT'  :'Linear Regression Intercept            ',
            'LINEARREG_SLOPE'      :'Linear Regression Slope                ',
            'STDDEV'               :'Standard Deviation                     ',
            'TSF'                  :'Time Series Forecast                   ',
            'VAR'                  :'Variance                               '}
        self.create_buttons(tab0,list(self.Grp_custom.keys()))
        
        self.create_label1(tab0,'Symbol:',3,2)
        self.entrys.addsymb=self.create_entry1(tab0,3,3)
        
        self.create_label1(tab0,'From File:',4,2)
        self.entrys.loadsymb=self.create_entry1(tab0,4,3)
        
        self.create_label1(tab0,'Period',5,2)
        self.entrys.pd=self.create_entry1(tab0,5,3)
        self.create_label1(tab0,'Ndays',5,4)
        self.entrys.ndays=self.create_entry1(tab0,5,5)
        
        self.create_buttons(tab1,list(self.Grp_overlay.keys()))
        self.create_buttons(tab2,list(self.Grp_momentum.keys())) 
        self.create_buttons(tab3,list(self.Grp_volum.keys())) 
        self.create_buttons(tab4,list(self.Grp_cycle_ind.keys())) 
        self.create_buttons(tab5,list(self.Grp_price_trans.keys())) 
        self.create_buttons(tab6,list(self.Grp_volatility.keys())) 
        self.create_buttons(tab7,list(self.Grp_pattern.keys())) 
        self.create_buttons(tab8,list(self.Grp_stat.keys())) 
        
                     
        # - - - - - - - - - - - - - - - - - - - - -
        # Quit button in the lower right corner
        quit_button = ttk.Button(self.window, text="Quit", command=self.window.destroy)
        quit_button.grid(row=1, column=3)
#%%  
class AddTreeView():
    def __init__(self, parent,g):
        self.tree=ttk.Treeview(parent)
        self.g=g
        for symb in g.d.symb:
           self.tree.insert("" , "end",  text=symb)
        self.tree.bind("<Double-1>", self.OnDoubleClick)
    def OnDoubleClick(self,event):
        item = self.tree.selection()[0]
        print("you clicked on", self.tree.item(item,"text"))
        self.g.plot_tk(self.tree.item(item,"text"))
    def update(self,symbs):
        self.tree.delete(*self.tree.get_children())
        for symb in symbs:
           self.tree.insert("" , "end",  text=symb)
        self.tree.bind("<Double-1>", self.OnDoubleClick)