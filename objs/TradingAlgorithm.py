# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:01:24 2019

@author: kuifenhu
"""
import pandas as pd
from datetime import datetime

class TradingAlgorithmObj:
  def __init__(self,result):
    self.result=result
    self.tafa_result=pd.DataFrame()
    self.mm_result=[]
    

#%%
  def tafa(self,n):
      writer = pd.ExcelWriter('./data/result_tafa'+datetime.now().strftime('%m_%d_%Y')+'.xlsx', engine='openpyxl') 
      for sec in self.result.keys():
          self.result[sec].xray()
          a=self.result[sec].summary.copy()
          a['PHealth']=round((a['Proic']+a['Proa']+a['Proe']+a['Pdebt']+a['Pldebt']+a['Pfcf']+a['Pgrossmargin']+a['Popermargin']+a['Pprofitmargin'])/9*20,2)
          a['PGrowth']=round((a['PEPSQQ']+a['PSaleQQ']+a['PEPSNext5Y']+a['PEPSthisY']+a['PSalespast5Y']+a['PEPSpast5Y']+a['Ppeg'])/7*20,2)
          a['PValue']=round((a['Pfpe']+a['Ppe']+a['Ppb']+a['Pps'])/4*20,2)
          a['PDiv']=round((a['Ppayout']+a['Pdivdend'])/2*20,2)
          a['PTechnical']=round((a['Ppricerange']+a['Prsi']+a['Pshort']+a['Pvol']+a['Pinst']+a['Pinsider']+a['Psma1']+a['Psma2'] + a['Psma3'])/9*20,2)
          a['Total']=round(0.35*a['PHealth']+0.35*a['PGrowth']+0.1*a['PValue']+0.1*a['PDiv']+0.1*a['PTechnical'],2)
          a['Total']['Mean']=100
          a['Total']['STD']=99
          
          a.sort_values(by='Total',ascending=False).to_excel(writer, sheet_name=sec)
      writer.save()
      writer.close() 
  #%%
  def newlow(self,n):
      writer = pd.ExcelWriter('./data/result_newlow.xlsx', engine='openpyxl') 
      for sec in self.result.keys():
          a=self.result[sec].summary.copy()
          a['Total']=round((a['Ppricerange']+a['Pvol'])/2*20,2)
          a.sort_values(by='Total',ascending=False).to_excel(writer, sheet_name=sec)
      writer.save()
      writer.close()
  #%%
  def mm(self,n):
      writer = pd.ExcelWriter('./data/result_newlow.xlsx', engine='openpyxl') 
      for sec in self.result.keys():
          a=self.result[sec].finviz_df.copy()
          Total=round((a['Ppricerange']+a['Pvol'])/2*20,2)
          Total.sort_values(ascending=False).to_excel(writer, sheet_name=sec)
      writer.save()
      writer.close()
  #%%    
  def diff(self):
      diff_result=pd.DataFrame()
      for sector in self.result.keys():
          for tk in self.result[sector].ts.keys():
            result1=(self.result[sector].ts[tk]['Close'].iloc[-1]-self.result[sector].ts[tk]['Close'].iloc[-2])/self.result[sector].ts[tk]['Close'].iloc[-2]
            df1=pd.DataFrame([result1],columns=['Diff_Close'],index={tk})       
            diff_result=diff_result.append(df1)
      return(diff_result)
      
     