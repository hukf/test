# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 08:40:52 2018

@author: kuifenhu
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from matplotlib.dates import DateFormatter, WeekdayLocator,DayLocator,MinuteLocator,HourLocator, MONDAY,MonthLocator
#from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
# pip install mpl_finance
from mpl_finance import candlestick_ohlc

import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.widgets import Button,Cursor,MultiCursor
from matplotlib.text import Text
import matplotlib.gridspec as gridspec
import talib as ta
'''
Download TA_Lib-0.4.10-cp27-cp27m-win_amd64.whl from http://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib.
And use command
pip install TA_Lib-0.4.10-cp27-cp27m-win_amd64.whl
'''

import numpy as np
import sys
import math
from matplotlib.backend_bases import MouseEvent
#%%


class GuiObj:
  def __init__(self,d):
    self.d=d
    self.ind=0
   
#%%
  def onclick(self,event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
#   event.dblclick =True/False
#   event.button= 1 ,2,3
#   location in pxial event.x event.y
#   event data   xdata and y data is the value in scale. 
#%% 
  def press(self,event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'l':
       print('into line mode')
       self.draggableline=DraggablePlot(self.fig_ohlc,self.ax)
#        visible = xl.get_visible()
#        xl.set_visible(not visible)
#        fig.canvas.draw()
#%% 
  def chart_ohlc(self):
    n_groups = len(self.d.symb)  
    self.fig_ohlc = plt.figure(figsize=(18, 10))
    self.cid1 = self.fig_ohlc.canvas.mpl_connect('button_press_event', self.onclick)
    self.cid2 = self.fig_ohlc.canvas.mpl_connect('key_press_event', self.press)
    gs = gridspec.GridSpec(2, 1,
#                       width_ratios=[1, 2],
                       height_ratios=[4, 1] )
    self.ax = self.fig_ohlc.add_subplot(gs[0])#,sharex=True)
    self.ax1 = self.fig_ohlc.add_subplot(gs[1],sharex=self.ax)
    
    self.months = MonthLocator()  
    self.months.MAXTICKS = 1500      # major ticks on the mondays
    self.mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    self.mondays.MAXTICKS = 1500      # major ticks on the mondays
    self.alldays = DayLocator()              # minor ticks on the days
    self.hoursloc = HourLocator()              # minor ticks on the days
    self.minloc = MinuteLocator()        # major ticks on the mondays
    self.monthFormatter = DateFormatter('%b %d')  # e., Jan 12
    self.weekFormatter = DateFormatter('%b %d')  # e., Jan 12
    self.dayFormatter = DateFormatter('%d')      # e., 12
    self.minFormatter=DateFormatter('%X')
  
    self.ax.xaxis.set_major_locator(self.months) 
    self.ax1.xaxis.set_major_locator(self.months) 
    self.d.selected_set=self.d.ts_result[0]
    self.plot_ohlc()
#    Text(0.5,1,ts[0]['symbol'])
    #        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    self.bnext = Button(axnext, 'Next')
    self.bnext.on_clicked(self.bt_next)
    self.bprev = Button(axprev, 'Previous')
    self.bprev.on_clicked(self.bt_prev)
    self.multi = MultiCursor(self.fig_ohlc.canvas, (self.ax, self.ax1), color='r', lw=1)
    self.cursor=Cursor(self.ax,useblit=True, color='red', linewidth=2)
    plt.show()

  def bt_next(self,event):
            self.ind += 1
            if self.ind>=len(self.d.ts_result):
                self.ind=0
            self.d.selected_set=self.d.ts_result[self.ind]
            self.plot_ohlc()
      
  def bt_prev(self,event):
            self.ind -= 1
            if self.ind<0:
                self.ind=len(self.d.ts_result)-1
     
            self.d.selected_set=self.d.ts_result[self.ind]
            self.plot_ohlc()
    
#%% plot ohlc
  def plot_tk(self,tk):
      #given the tk symb, find the index and set to the selected holder and plot it. 
      self.d.selected_set=self.d.ts_result[self.d.symb.index(tk)]
      self.plot_ohlc()
  def plot_ohlc(self):
            plt.sca(self.ax)
            self.ax.cla()
            self.ax1.cla()
            if self.d.selected_set.size==0:
                print('Error: No data set is selected to display')
                return
            dt=self.d.selected_set[1,0]-self.d.selected_set[0,0]
            if dt>0.05:
               widthtmp=0.6
            else:
               widthtmp=0.0003
               
            candlestick_ohlc(self.ax, self.d.selected_set, width=widthtmp, colorup='#77d879', colordown='#db3f3f') 
            if len(self.d.holdings)>0:
                try:
                    holding=self.d.holdings[self.d.ts[self.ind]['symbol']]
                    plt.axhline(y=holding,linewidth=4, color='r')
                except:
                    pass
            plt.subplots_adjust(bottom=0.2) 
            
            plt.title(self.d.ts[self.ind]['symbol'])
            for label in self.ax.xaxis.get_ticklabels():
                label.set_rotation(0)
            self.ax.grid(True)
            self.ax.xaxis_date()
            self.ax.autoscale_view()
            plt.sca(self.ax1)
            plt.bar(self.d.ts_result[self.ind][:,0],self.d.ts_result[self.ind][:,-1],width =widthtmp)     
            
            if self.d.period>=5:
               self.ax.xaxis.set_major_locator(self.months)
               self.ax.xaxis.set_minor_locator(self.mondays)
               self.ax.xaxis.set_major_formatter(self.monthFormatter)
               self.ax1.xaxis.set_major_locator(self.months)
               self.ax1.xaxis.set_minor_locator(self.mondays)
               self.ax1.xaxis.set_major_formatter(self.monthFormatter)
            
            elif self.d.period>=1:
               
               self.ax.xaxis.set_major_locator(self.mondays)
              # self.ax.xaxis.set_minor_locator(self.alldays)
               self.ax.xaxis.set_major_formatter(self.weekFormatter)
               self.ax1.xaxis.set_major_locator(self.mondays)
              # self.ax1.xaxis.set_minor_locator(self.alldays)
               self.ax1.xaxis.set_major_formatter(self.weekFormatter)

            else:
               
               self.ax.xaxis.set_major_locator(self.hoursloc)
               self.ax.xaxis.set_minor_locator(self.minloc)
               self.ax.xaxis.set_major_formatter(self.minFormatter)
               self.ax1.xaxis.set_major_locator(self.hoursloc)
               self.ax1.xaxis.set_minor_locator(self.minloc)
               self.ax1.xaxis.set_major_formatter(self.minFormatter)
               
            self.multi = MultiCursor(self.fig_ohlc.canvas, (self.ax, self.ax1), color='r', lw=1)
            self.cursor=Cursor(self.ax,useblit=True, color='red', linewidth=0.2)
            
            plt.draw()
            
#%%
  def cursor(self):
#%%
    self.cursor = Cursor(self.ax, useblit=True, color='red', linewidth=2)

         
  def chart_keys(self):
        n_groups = len(self.d.keys_result)  
        m=np.ceil(n_groups/4)
        index=np.arange(n_groups)
        bar_width = 0.1
        opacity = 1
        error_config = {'ecolor': '0.3'}
        cor=('r','g','b','k','y')
        xticklabel=[]
        self.fig_keys = plt.figure(figsize=(19, 10))
#        fig1 = plt.figure(figsize=(8, 32))
        
        for ID in index:  
         symb=self.d.keys_result[ID]['symbol']
         ax = self.fig_keys.add_subplot(m,4,ID+1)
         ax1=self.fig_keys.add_subplot(m,4,ID+1)
         v=self.d.keys_result[ID]['keys'][symb]['marketcap']
         marketcap=(0 if v is None else v)
         v=self.d.keys_result[ID]['keys'][symb]['dividendYield']
         dividendYield=(0 if v is None else v)
         companyname=self.d.keys_result[ID]['keys'][symb]['companyName']
         
#              
         for PD in np.flip(np.arange(4),0):
#            cashChange=self.d.keys_result[ID]['financial'][symb][PD]['cashChange']
#            cashFlow=self.d.keys_result[ID]['financial'][symb][PD]['cashFlow']
#            costOfRevenue=self.d.keys_result[ID]['financial'][symb][PD]['costOfRevenue']
#            currentAssets=self.d.keys_result[ID]['financial'][symb][PD]['currentAssets']
#            currentCash=self.d.keys_result[ID]['financial'][symb][PD]['currentCash']
#            currentDebt=self.d.keys_result[ID]['financial'][symb][PD]['currentDebt']
            v=self.d.keys_result[ID]['financial'][symb][PD]['grossProfit']
            grossProfit=(0 if v is None else v)
            v=self.d.keys_result[ID]['financial'][symb][PD]['netIncome']
            netIncome=(0 if v is None else v)
#            operatingExpense=self.d.keys_result[ID]['financial'][symb][PD]['operatingExpense']
#            operatingGainsLosses=self.d.keys_result[ID]['financial'][symb][PD]['operatingGainsLosses']
            v=self.d.keys_result[ID]['financial'][symb][PD]['operatingIncome']
            operatingIncome=(0 if v is None else v)
#            operatingRevenue=self.d.keys_result[ID]['financial'][symb][PD]['operatingRevenue']
            reportDate=self.d.keys_result[ID]['financial'][symb][PD]['reportDate']
#            researchAndDevelopment=self.d.keys_result[ID]['financial'][symb][PD]['researchAndDevelopment']
            v=self.d.keys_result[ID]['financial'][symb][PD]['shareholderEquity']
            shareholderEquity=(0 if v is None else v)
            v=self.d.keys_result[ID]['financial'][symb][PD]['totalAssets']
            totalAssets=(0 if v is None else v)
            v=self.d.keys_result[ID]['financial'][symb][PD]['totalCash']
            totalCash=(0 if v is None else v)
           
#            totalDebt=self.d.keys_result[ID]['financial'][symb][PD]['totalDebt']
#            totalLiabilities=self.d.keys_result[ID]['financial'][symb][PD]['totalLiabilities']#            
            v=self.d.keys_result[ID]['financial'][symb][PD]['totalRevenue']
            totalRevenue=(0 if v is None else v)
            v=self.d.keys_result[ID]['earnings'][symb][PD]['actualEPS']
            actualEPS=(0 if v is None else v)
            v=self.d.keys_result[ID]['earnings'][symb][PD]['estimatedEPS']
            estimatedEPS=(0 if v is None else v)
            v=self.d.keys_result[ID]['earnings'][symb][PD]['consensusEPS']
            consensusEPS=(0 if v is None else v)
            v=self.d.keys_result[ID]['earnings'][symb][PD]['EPSReportDate']
            EPSReportDateS=(0 if v is None else v)
#            v=self.d.keys_result[ID]['earnings'][symb][PD]['estimateEPS']
#            estimateEPS=(0 if v is None else v)
            
            
            xticklabel.append(reportDate)  
            BalanceSheet = [totalAssets, shareholderEquity,totalCash]
            Income = [totalRevenue,grossProfit,operatingIncome,netIncome]
            earning=[estimatedEPS ]
            rects0=[]
            rects1=[]
            rects2=[]
            k=0
            for i in BalanceSheet:
                rects0.append(ax.bar(3-PD, marketcap, bar_width,
                            alpha=0.5, color='m',edgecolor = 'k',
                           # yerr=std_men, error_kw=error_config,
                            label='BalanceSheet'))
                rects1.append(ax.bar(3-PD+bar_width, i, bar_width,
                            alpha=1, color=cor[k],edgecolor = 'k',
                           # yerr=std_men, error_kw=error_config,
                            label='BalanceSheet'))
                k=k+1
                
            k=0    
            for i in Income:    
                rects2.append(ax.bar(3-PD + 2*bar_width, i, bar_width,
                            alpha=opacity, color=cor[k],edgecolor = 'k',
            #                yerr=std_women, error_kw=error_config,
                            label='Income'))
                k=k+1
              
            
        
#         ax.set_xlabel('Date')
         ax.set_ylabel('Value')
         ax.set_title(symb+'::'+companyname+ ':'+"%2.2f" % dividendYield)
         ax.set_xticks(np.arange(4) + bar_width / 2)
         ax.set_xticklabels(tuple(xticklabel))
#           ax.legend()
          
#         fig.tight_layout()
         plt.show()



class DraggablePlot(object):
    u""" An example of plot with draggable markers """

    def __init__(self,fig,ax):
        self._figure=fig
        self._axes=ax
        self._line = None
        self._dragging_point = None
        self._points = {}

        self._init_plot()

    def _init_plot(self):
#        self._figure = plt.figure("Example plot")
#        axes = plt.subplot(1, 1, 1)
#        axes.set_xlim(0, 100)
#        axes.set_ylim(0, 100)
#        axes.grid(which="both")
        

        self._figure.canvas.mpl_connect('button_press_event', self._on_click)
        self._figure.canvas.mpl_connect('button_release_event', self._on_release)
        self._figure.canvas.mpl_connect('motion_notify_event', self._on_motion)
#        plt.show()

    def _update_plot(self):
        if not self._points:
            return
        x, y = zip(*sorted(self._points.items()))
        # Add new plot
        if not self._line:
            self._line, = self._axes.plot(x, y, "b", marker="o", markersize=10)
        # Update current plot
        else:
            self._line.set_data(x, y)
        self._figure.canvas.draw()

    def _add_point(self, x, y=None):
        if isinstance(x, MouseEvent):
            x, y = int(x.xdata), int(x.ydata)
        self._points[x] = y
        return x, y

    def _remove_point(self, x, _):
        if x in self._points:
            self._points.pop(x)

    def _find_neighbor_point(self, event):
        u""" Find point around mouse position
        :rtype: ((int, int)|None)
        :return: (x, y) if there are any point around mouse else None
        """
        distance_threshold = 3.0
        nearest_point = None
        min_distance = math.sqrt(2 * (100 ** 2))
        for x, y in self._points.items():
            distance = math.hypot(event.xdata - x, event.ydata - y)
            if distance < min_distance:
                min_distance = distance
                nearest_point = (x, y)
        if min_distance < distance_threshold:
            return nearest_point
        return None

    def _on_click(self, event):
        u""" callback method for mouse click event
        :type event: MouseEvent
        """
        # left click
        if event.button == 1 and event.inaxes in [self._axes]:
            point = self._find_neighbor_point(event)
            if point:
                self._dragging_point = point
                self._remove_point(*point)
            else:
                self._add_point(event)
            self._update_plot()
        # right click
        elif event.button == 3 and event.inaxes in [self._axes]:
            point = self._find_neighbor_point(event)
            if point:
                self._remove_point(*point)
                self._update_plot()

    def _on_release(self, event):
        u""" callback method for mouse release event
        :type event: MouseEvent
        """
        if event.button == 1 and event.inaxes in [self._axes] and self._dragging_point:
            self._add_point(event)
            self._dragging_point = None
            self._update_plot()

    def _on_motion(self, event):
        u""" callback method for mouse motion event
        :type event: MouseEvent
        """
        if not self._dragging_point:
            return
        self._remove_point(*self._dragging_point)
        self._dragging_point = self._add_point(event)
        self._update_plot()
       