# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:16:35 2018

@author: kuifenhu
"""
import numpy as np
import talib as ta

t=p1.d.ts_result[0][:,0]
op=p1.d.ts_result[0][:,1]
high=p1.d.ts_result[0][:,2]
low=p1.d.ts_result[0][:,3]
close=p1.d.ts_result[0][:,4]
vol=p1.d.ts_result[0][:,5]

output = ta.SMA(close)

x=np.transpose(p1.d.selected_set[:,0])
y=ta.SMA(p1.d.selected_set[:,4])
plt.sca(p1.g.ax)
plt.plot(x,y)

ef add_series(x, id):
  plt.plot(x, gid = id)

def remove_series(id):
  for c in plt.collections:
    if c.get_gid() == id:
      c.remove()
      