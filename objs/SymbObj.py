# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:09:19 2018

@author: kuifenhu
"""
import pandas as pd
import easygui
from yahoo_fin import stock_info as si
#%%
class SymbObj:
  def __init__(self):
    self.symb=['AAPL']
    self.sector={'holding':['AAPL']}   
    self.symb_all=[]
    self.sp500=[]
  def loadfromfile(self):

    #fname=easygui.fileopenbox(msg='Load the investment idea excel file', title=None, default='Investment ideas.xlsm', filetypes='*.xlsm', multiple=False)
    fname='Investment ideas.xlsm'
    df= pd.read_excel(fname, header=[0], sheetname='sp500')
    
    sectorname=df.Sector.unique().tolist()  
    symb3={}
    for sector in sectorname:
        tmp=df['Symbol'].loc[df['Sector']==sector].tolist()
        symb3.update({sector:tmp})
    self.sector.update(symb3)
    
  def loadsymb(self):
    df=pd.DataFrame.from_csv('sp500Symbol_p.csv')
    self.symb=df['Symbol'].tolist()
  def sp500(self):
      self.symb=si.tickers_sp500()
  def dow(self):
      self.symb=si.tickers_dow()
  def nasdaq(self):
      self.symb=si.tickers_nasdaq()
  def others(self):
      self.symb=si.tickers_other()
  def holding(self):    
      self.symb=stocklist1=pd.read_csv('companylistNYSE.csv')
      
#%%
  def load_symbols(self):
      [self.symb_all,self.symb_sp500]=load_symbols()
#%%

def load_symbols(self):
    #download form https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=AMEX
    stocklist1=pd.read_csv('companylistNYSE.csv')
    stocklist2=pd.read_csv('companylistNasdaq.csv')
    stocklist3=pd.read_csv('companylistamex.csv')
    stocklist=[stocklist1,stocklist2,stocklist3]
    symbols=pd.concat(stocklist)
    # condition some financial data
    symbols['MarketCap']=symbols['MarketCap'].replace('n/a', 'nan', regex=True)
    symbols['MarketCap']=symbols['MarketCap'].replace('B', '000000000', regex=True)
    symbols['MarketCap']=symbols['MarketCap'].replace('M', '000000', regex=True)
    symbols['MarketCap']=symbols['MarketCap'].replace('K', '000', regex=True)
    symbols['MarketCap']=symbols['MarketCap'].replace('[ZO\$,.]', '', regex=True).astype(float)
    
    #download form https://www.nasdaq.com/etfs/list 
    etflist=pd.read_csv('ETFList.csv')
    etflist[etflist['Symbol']=='spy'.upper()]
    etflist[etflist['Name'].str.contains('SPDR')]
    tmp1=etflist.drop(etflist.columns[2:],axis=1)
    for i in [2,3,4,7,8]:
        tmp1[symbols.columns[i]]=0
    tmp1['Sector']='ETF'
    tmp1['industry']='ETF'
    # change the ETF format to merge with stock list. 
    
    symbol=pd.concat([symbols,tmp1],axis=0,ignore_index=True,sort=True)
    #symbol.index=pd.RangeIndex(len(symbol.index))
    # list of SP500 https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
    sp500=pd.read_csv('SP500list.csv',encoding = "ISO-8859-1")
    
    # find a row with string 
    symbols[symbols['Symbol'].str.contains('A'.upper())]
    symbols[symbols['Symbol']=='QQQ'.upper()]
    
    # find a row in a column
    symbol500=symbols.loc[symbols['Symbol'].isin(sp500['Ticker'])]
   # symbol500.reset_index(drop=True)
    symbol500.index=pd.RangeIndex(len(symbol500.index))
    self.symbol=symbol
    self.symbol500=symbol500
#    [a,b]=load_symbols()
#    
#    b.to_csv('sp500Symbol_p.csv', sep=',', encoding='utf-8')
#    a.to_csv('Symbolall_p.csv', sep=',', encoding='utf-8')


#a=LoadsymbObj()
#a.loadsymb()