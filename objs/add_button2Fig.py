# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:06:55 2018

@author: kuifenhu
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

fig = plt.figure(figsize=(150, 32))
ax = fig.add_subplot(1,1,1)#,sharex=True)
candlestick_ohlc(ax, result[0], width=0.6, colorup='#77d879', colordown='#db3f3f') 

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12
plt.subplots_adjust(bottom=0.2) 
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)      
#ax.xaxis.set_minor_formatter(dayFormatter)
#plot_day_summary(ax, quotes, ticksize=3)
         
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(0)
#        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#        ax.xaxis.set_major_locator(mticker.MaxNLocator(10))
ax.grid(True)
ax.xaxis_date()
ax.autoscale_view()
plt.title(ts[0]['symbol'])
Text(0.5,1,ts[0]['symbol'])
#        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


class Index(object):
    ind = 0

    def next(self, event):
        plt.sca(ax)
        ax.cla()
        self.ind += 1
        if self.ind>=n_groups:
            self.ind=0
        candlestick_ohlc(ax, result[self.ind], width=0.6, colorup='#77d879', colordown='#db3f3f') 
 
        plt.subplots_adjust(bottom=0.2) 
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
        ax.xaxis.set_major_formatter(weekFormatter)
        plt.title(ts[self.ind]['symbol'])
        plt.draw()

    def prev(self, event):
        plt.sca(ax)
        plt.cla()
        self.ind -= 1
        if self.ind<0:
            self.ind=n_groups-1
        candlestick_ohlc(ax, result[self.ind], width=0.6, colorup='#77d879', colordown='#db3f3f') 
 
        plt.subplots_adjust(bottom=0.2) 
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
        ax.xaxis.set_major_formatter(weekFormatter)
        plt.title(ts[self.ind]['symbol'])
        plt.draw()

callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.show()
