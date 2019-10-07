# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 08:50:33 2018

@author: kuifenhu
"""

#%%
# Credit: Josh Hemann

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 4

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}
cor=('r','b','g','k','y')
for j in index:
    ID=j
    PD=0
    symb=p1.keys_result[ID]['symbol']
    totalAssets=p1.keys_result[ID]['financial'][symb][PD]['totalAssets']
    cashChange=p1.keys_result[ID]['financial'][symb][PD]['cashChange']
    cashFlow=p1.keys_result[ID]['financial'][symb][PD]['cashFlow']
    costOfRevenue=p1.keys_result[ID]['financial'][symb][PD]['costOfRevenue']
    currentAssets=p1.keys_result[ID]['financial'][symb][PD]['currentAssets']
    currentCash=p1.keys_result[ID]['financial'][symb][PD]['currentCash']
    currentDebt=p1.keys_result[ID]['financial'][symb][PD]['currentDebt']
    grossProfit=p1.keys_result[ID]['financial'][symb][PD]['grossProfit']
    netIncome=p1.keys_result[ID]['financial'][symb][PD]['netIncome']
    operatingExpense=p1.keys_result[ID]['financial'][symb][PD]['operatingExpense']
    operatingGainsLosses=p1.keys_result[ID]['financial'][symb][PD]['operatingGainsLosses']
    operatingIncome=p1.keys_result[ID]['financial'][symb][PD]['operatingIncome']
    operatingRevenue=p1.keys_result[ID]['financial'][symb][PD]['operatingRevenue']
    reportDate=p1.keys_result[ID]['financial'][symb][PD]['reportDate']
    researchAndDevelopment=p1.keys_result[ID]['financial'][symb][PD]['researchAndDevelopment']
    shareholderEquity=p1.keys_result[ID]['financial'][symb][PD]['shareholderEquity']
    totalAssets=p1.keys_result[ID]['financial'][symb][PD]['totalAssets']
    totalCash=p1.keys_result[ID]['financial'][symb][PD]['totalCash']
    totalDebt=p1.keys_result[ID]['financial'][symb][PD]['totalDebt']
    totalLiabilities=p1.keys_result[ID]['financial'][symb][PD]['totalLiabilities']
    totalRevenue=p1.keys_result[ID]['financial'][symb][PD]['totalRevenue']
    
    BalanceSheet = [totalAssets, shareholderEquity,totalCash]
    Income = [totalRevenue,grossProfit,operatingIncome,netIncome]

    rects1=[]
    rects2=[]
    k=0
    for i in BalanceSheet:
        rects1.append(ax.bar(j, i, bar_width,
                    alpha=1, color=cor[k],
                   # yerr=std_men, error_kw=error_config,
                    label='BalanceSheet'))
        k=k+1
    k=0    
    for i in Income:    
        rects2.append(ax.bar(j + bar_width, i, bar_width,
                    alpha=opacity, color=cor[k],
    #                yerr=std_women, error_kw=error_config,
                    label='Income'))
        


ax.set_xlabel('Group')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
ax.legend()

fig.tight_layout()
plt.show()
