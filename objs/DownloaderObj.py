# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:34:37 2018

@author: kuifenhu
"""
from objs.PY_downloader2 import get_ticker_update
# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
from datetime import datetime, timedelta
from scipy import io as sio 
from time import time
from pandas import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from objs.finvizObj import finvizObj
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

import asyncio


class data_holder(object):
    pass

#%%
class DownloaderObj:
  def __init__(self,s):
    self.s=s
    self.symb=s.symb
    self.period=1 # selected interval  default is 1 day. less than 1 would be day chart. larger than one would be weekly monthly chart
    self.ndays=100 # retreive the history data back in ndays. default is 500
    self.ts_result=[]
    self.keys_result=[]
    self.pulse_result=[]
    self.realtime_result=[]
    self.selected_set=[]
    self.holdings={}

#%%
  def Download_ts(self):
      if self.period>=1:
          self.Download_daychart()
      else:
          self.Download_minchart()
  def Download_realtime(self):
        self.realtime_result=[]
        n=0
        for symb in self.symb:
          try:
             
             print('TK'+str(n) +' :: '+symb + ' Real time downloaded')
             self.realtime_result.append(si.get_live_price(symb))
             n=n+1
          except:
             self.realtime_result.append(0)
             
             print('TK'+str(n) +' :: '+symb + ' download failed')
             n=n+1
             continue
        print('_____________Real Time Download Done________________') 
        
  def Download_quotetb(self):
        self.quotetb_result=[]
        n=0
        for symb in self.symb:
          try:
             
             print('TK'+str(n) +' :: '+symb + ' Quote Table downloaded')
             self.quotetb_result.append(si.get_quote_table(symb,dict_result=False))
             n=n+1
          except:
             self.quotetb_result.append(0)
             
             print('TK'+str(n) +' :: '+symb + ' Quote Table download failed')
             n=n+1
             continue
        print('_____________Quote Table Download Done________________')
        
  def Download_pulse(self):
        self.pulse_result={}
        # get most active stocks on the day
        if asyncio.get_event_loop().is_running(): # Only patch if needed (i.e. running in Notebook, Spyder, etc)
            import nest_asyncio
            nest_asyncio.apply()

        self.pulse_result['most_active']=si.get_day_most_active()
         
        # get biggest gainers
        self.pulse_result['gainer']=si.get_day_gainers()
         
        # get worst performers
        self.pulse_result['loser']=si.get_day_losers()
        print('_____________Market Pulse Download Done________________')  
        
#get_analysts_info
#get_balance_sheet
#get_cash_flow
#get_data
#get_day_gainers
#get_day_losers
#get_day_most_active
#get_holders
#get_income_statement
#get_live_price
#get_quote_table
#get_top_crypto
#get_stats
#tickers_dow
#tickers_nasdaq
#tickers_other
#tickers_sp500


  
          
  def Download_daychart(self,n):
        self.ndays=n
        # set paramter p1.g.pd as period.
        # holder for raw data in dataframe format. just get the ticker header.
        n_groups = len(self.symb)  
        self.ts=get_ticker_update(self.symb,self.ndays)
        # data holder for the re-orged into np arrary format, with selected period interval
#        self.ts_result={}
#        n=len(self.ts)
#        ohlc = []
#        # loop each ticker saved in the ts. ts.data ts.t ts.symbol  
#        for i in np.arange(n):
#            # check the total record of ts. 
#            y=len(self.ts[i]['t'])
#            x=0
#            ohlc=[]
#            # what I am doing here?
#            while x < y:
#                k=0
#                hi2=0
#                lo2=1e5
#                vol=0
#                while k<self.period and x < y:
#                    if k==0: 
#                        t2=mdates.date2num(datetime.strptime(self.ts[i]['t'][x],"%Y-%m-%d"))
#                        #t2=mdates.date2num(self.ts[i]['t'][x].strftime("%Y-%m-%d"))
#                        #t2=mdates.date2num(self.ts[i]['t'][x])
#                        
#                        op2=self.ts[i]['data']['Open'][x]
#                    if k==self.period-1 or x==y-1:
#                        cl2=self.ts[i]['data']['Close'][x]
#                        cl1=self.ts[i]['data']['Adj_Close'][x]
#                        
#                    if hi2< self.ts[i]['data']['High'][x]:
#                        hi2=self.ts[i]['data']['High'][x]
#                    if lo2> self.ts[i]['data']['Low'][x]:
#                        lo2=self.ts[i]['data']['Low'][x] 
#                    vol=vol+self.ts[i]['data']['Volume'][x]
#                    k=k+1    
#                    x=x+1    
#                append_me = [t2, op2,hi2,lo2,cl1,cl2,vol] 
#                symb=self.ts[i]['symbol']
#                
#            self.ts_result.update({symb:np.array(append_me)})
        print('_____________Historical data Download Done________________') 
                

  def Download_finviz(self):
      a=finvizObj()
      t0=time()
      k=0
      self.finviz_result=[]
      for symb1 in self.symb:
          try:
              tmp=a.get_keys(symb1)
              tmp1=pd.DataFrame([tmp],columns=tmp.keys())
              tmp1['symb']=symb1
              tmp1['status']=1
              
              self.finviz_result.append(tmp1)              
              print('TK'+str(k)+' :: ' +symb1+' key matrix from Finviz is loaded sucessfully')
          except:
              #tmp1['status']=0
              #tmp1['symb']=symb1
              #self.finviz_result.append(tmp1)              
              print('TK'+str(k)+' :: ' +symb1+' Load error in finviz parser, Check symbol please')
              continue

          k=k+1
      print('_____________Key ratios from Finviz Download______________________')
      print('All done Total time '+str(int(time()-t0))+' Seconds')     
#%%
  def peers(self,symb):
                tsla = Stock(symb,output_format='pandas')
                relevant=tsla.get_relevant()
                df1=relevant.to_dict()
                return df1[symb]['symbols']
#%%
  def damp2csv(self):
      i=0
      for symb1 in self.symb: 
        np.savetxt('./data/'+symb1+'.csv',self.ts_result[i],delimiter=',')
        i=i+1
  def damp2mat(self):
#      symbol: {'IPG'}
#      data: [4734×8 double]
#         t: [4734×1 double]
     i=0
     for symb1 in self.symb: 
       d={'symbol':symb1,'t':self.ts.result[i][:,0],'data':self.ts.result[i][:,1:]}  
       df=pd.DataFrame(data=d)
       df.data.reset_index(level=0,inplace=True)
       scipy.io.savemat('test.mat',{'struct':df.to_dict('list')})
       i=i+1
  def alert(self):
      # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    #with open(textfile, 'rb') as fp:
        # Create a text/plain message
    str1='test'
    msg = MIMEText(str1)
    
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'The contents of test' # textfile
    msg['From'] ='dvdenv@yahoo.com'
    msg['To'] = 'kuifeng@gmail.com'
    
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP_SSL("smtp.mail.yahoo.com",465)
   # s.starttls()
    s.ehlo()
    
    s.login('dvdenv','Keysight4U')
    try :
        s.sendmail('dvdenv@yahoo.com', 'kuifeng@gmail.com', msg.as_string())
        s.quit()
        print('ok the email has sent ')
    except :
        print('can\'t send the Email')
    
   
  def xray(self): 
      
    # convert the finviz_result into dataframe    
    self.finviz_df=pd.DataFrame()
    self.summary=pd.DataFrame()
    x=0
    for x in np.arange(start=0,stop=len(self.finviz_result),step=1):
        self.finviz_df=self.finviz_df.append(self.finviz_result[x])
    self.finviz_df=self.finviz_df.set_index('symb')

# calculate the mean and standard diviation 


# calcuate the normaized key matrix
    
#for x in np.arange(start=0,stop=len(d.finviz_result),step=1):
    for index, row in self.finviz_df.iterrows():
      try:

            
       # print(index)
    #__________________ PHealth  ROI, ROA ROE Debt, FCF,_____________________
       
      #  print('_________PHealth____________')  
        key='ROA'
        Proa_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Proa_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Proa=intep3(self.finviz_df.loc[index,key],Proa_mean_val,Proa_std_val)
            
        key='ROE'
        Proe_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Proe_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Proe=intep3(self.finviz_df.loc[index,key],Proe_mean_val,Proe_std_val)
        
        key='ROI'
        Proic_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Proic_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Proic=intep3(self.finviz_df.loc[index,key],Proic_mean_val,Proic_std_val)
        
        key='P/FCF'
        Pfcf_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Pfcf_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Pfcf=intep_3(self.finviz_df.loc[index,key],Pfcf_mean_val,Pfcf_std_val)
    
        key='LTDebt/Eq'
        Pldebt_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Pldebt_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        if Proe==0:
            Pldebt=0
        else: 
            Pldebt=intep_3(self.finviz_df.loc[index,key],Pldebt_mean_val,Pldebt_std_val)
    
        key='Debt/Eq'
        Pdebt_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Pdebt_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)

        if Proe==0:
            Pdebt=0
        else:
            Pdebt=intep_3(self.finviz_df.loc[index,key],Pdebt_mean_val,Pdebt_std_val)
        
        key='GrossMargin'
        Pgrossmargin_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Pgrossmargin_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Pgrossmargin=intep3(self.finviz_df.loc[index,key],Pgrossmargin_mean_val,Pgrossmargin_std_val)
        
        key='Oper.Margin'
        Popermargin_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Popermargin_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Popermargin=intep3(self.finviz_df.loc[index,key],Popermargin_mean_val,Popermargin_std_val)
        
        key='ProfitMargin'
        Pprofitmargin_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Pprofitmargin_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Pprofitmargin=intep3(self.finviz_df.loc[index,key],Pprofitmargin_mean_val,Pprofitmargin_std_val)
        
        
        
     #__________________ PValue  Ppe, Pfpe,P/b, P/s, _______________    
     
     #   print('_________PValue____________')
        
        key='ForwardP/E'
        Pfpe_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Pfpe_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Pfpe=intep_3(self.finviz_df.loc[index,key],Pfpe_mean_val,Pfpe_std_val)
    
        key='P/E'
        Ppe_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Ppe_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Ppe=intep_3(self.finviz_df.loc[index,key],Ppe_mean_val,Ppe_std_val)
    
        key='P/B'
        Ppb_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Ppb_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Ppb=intep_3(self.finviz_df.loc[index,key],Ppb_mean_val,Ppb_std_val)
    
        key='P/S'
        Pps_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Pps_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Pps=intep_3(self.finviz_df.loc[index,key],Pps_mean_val,Pps_std_val)
    
           
    #__________________ PGrwoth  PEG_____________________
        
    #    print('_________PGrowth____________')
    
        key='PEG'
        Ppeg_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Ppeg_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Ppeg=intep_3(self.finviz_df.loc[index,key],Ppeg_mean_val,Ppeg_std_val)
        
      
#        
#        EPSNextQ=d.finviz_result[x]['EPSnextQ'][0]
#        PEpsNextQ=intep1(0, 0.25,EPSNexQ)
        
#        EPSnextY=d.finviz_result[x]['EPSnextY'][0]
#        PEpsNextY=intep3(EPSnextY/0.125,2,'EPSnextY%')
        
    
        key='EPSQ/Q'
        PEPSQQ_mean_val=self.finviz_df[(self.finviz_df[key]>0) & (self.finviz_df[key]<0.5)][key].mean(axis=0)
        PEPSQQ_std_val=self.finviz_df[(self.finviz_df[key]>0) & (self.finviz_df[key]<0.5 )][key].std(axis=0)
        PEPSQQ=intep3(self.finviz_df.loc[index,key],PEPSQQ_mean_val,PEPSQQ_std_val)
    
        key='SalesQ/Q'
        PSaleQQ_mean_val=self.finviz_df[(self.finviz_df[key]>0 ) & (self.finviz_df[key]<0.5) ][key].mean(axis=0)
        PSaleQQ_std_val=self.finviz_df[(self.finviz_df[key]>0 ) & (self.finviz_df[key]<0.5)][key].std(axis=0)
        PSaleQQ=intep3(self.finviz_df.loc[index,key],PSaleQQ_mean_val,PSaleQQ_std_val)
    
        key='EPSpast5Y'
        PEPSpast5Y_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        PEPSpast5Y_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        PEPSpast5Y=intep3(self.finviz_df.loc[index,key],PEPSpast5Y_mean_val,PEPSpast5Y_std_val)
        
        key='Salespast5Y'
        PSalespast5Y_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        PSalespast5Y_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        PSalespast5Y=intep3(self.finviz_df.loc[index,key],PSalespast5Y_mean_val,PSalespast5Y_std_val)
        
        key='EPSthisY'
        PEPSthisY_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        PEPSthisY_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        PEPSthisY=intep3(self.finviz_df.loc[index,key],PEPSthisY_mean_val,PEPSthisY_std_val)

        key='EPSnext5Y'
        PEPSNext5Y_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        PEPSNext5Y_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        PEPSNext5Y=intep3(self.finviz_df.loc[index,key],PEPSNext5Y_mean_val,PEPSNext5Y_std_val)
        


    

        
    #    EPSpast5Y=d.finviz_result[x]['EPSpast5Y'][0]
    #    PEpsPast5Y=intep_3(EPSpast5Y/0.125,1,'EPSpast5Y')
        
    #   PEpsNext=PEpsQQ*0.2+PSaleQQ*0.2+PEpsNext5Y*0.2+Ppeg*0.2
    
    
    
    
     #__________________ PTechnical Ppricerange, Psma1,2,3, Pvol,Prsi,Pshort, Pinst, Pinsider_______    
     
   #     print('_________PTechnical____________')
        price=self.finviz_df.loc[index,'Price']
        low=price/(1+self.finviz_df.loc[index,'52WLow'])
        high=price/(1+self.finviz_df.loc[index,'52WHigh'])
        Ppricerange_mean_val=0
        Ppricerange_std_val=0
        
        if price<=low:  
            Ppricerange=5
        elif price>high:
            Ppricerange=0
        else:
            k=5/(low-high)
            Ppricerange=round(k*(price-low)+5,2)
        #print('Ppricerange=',Ppricerange)  
        key='SMA20'
        Psma1_mean_val=self.finviz_df[(self.finviz_df[key]>0) ][key].mean(axis=0)
        Psma1_std_val=self.finviz_df[(self.finviz_df[key]>0)][key].std(axis=0)
        sma1=self.finviz_df.loc[index,key]
        
        key='SMA50'
        Psma2_mean_val=self.finviz_df[(self.finviz_df[key]>0) ][key].mean(axis=0)
        Psma2_std_val=self.finviz_df[(self.finviz_df[key]>0)][key].std(axis=0)
        sma2=self.finviz_df.loc[index,key]

        key='SMA200'
        Psma3_mean_val=self.finviz_df[(self.finviz_df[key]>0) ][key].mean(axis=0)
        Psma3_std_val=self.finviz_df[(self.finviz_df[key]>0)][key].std(axis=0)
        sma3=self.finviz_df.loc[index,key]
        
        if sma1<=-0.2:  
            Psma1=5
        elif sma1>=0.2:
            Psma1=0
        else:
            Psma1=round(-12.5*(sma1)+2.5,2)
            
        if sma2<=-0.2:  
            Psma2=5
        elif sma2>=0.2:
            Psma2=0
        else:
            Psma2=round(-12.5*(sma2)+2.5,2)
            
        if sma3<=-0.2:  
            Psma3=5
        elif sma3>=0.2:
            Psma3=0
        else:
            Psma3=round(-12.5*(sma3)+2.5,2)
        #print('sma20=',Psma1,'sma50=',Psma2,'sma200=',Psma3)

        key='RelVolume'
        Pvol_mean_val=self.finviz_df[(self.finviz_df[key]>0) ][key].mean(axis=0)
        Pvol_std_val=self.finviz_df[(self.finviz_df[key]>0)][key].std(axis=0)
        vol=self.finviz_df.loc[index,key]
        Pvol=intep4(vol,1,key)
        
        key='RSI(14)'
        Prsi_mean_val=self.finviz_df[(self.finviz_df[key]>0) ][key].mean(axis=0)
        Prsi_std_val=self.finviz_df[(self.finviz_df[key]>0)][key].std(axis=0)
        rsi=self.finviz_df.loc[index,key]
        Prsi=round(5-rsi/20,2)
        #print('Prsi=', rsi)
    
        key='ShortFloat'
        Pshort_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Pshort_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        Pshort=intep3(self.finviz_df.loc[index,key],Pshort_mean_val,Pshort_std_val)
      
        # range map [0-0.25] to [5:0]
        
        key='InsiderTrans'
        insider=self.finviz_df.loc[index,key]    
        if insider<=-0.2:  
            Pinsider=5
        elif insider>0.2:
            Pinsider=5
        else:
            Pinsider=round(25*insider,2)
        #print('Pinsider=', Pinsider)
        Pinsider_mean_val=0
        Pinsider_std_val=0
        
        inst=self.finviz_df.loc[index,'InstTrans']
        
        if inst<=-0.2:  
            Pinst=-5
        elif inst>0.2:
            Pinst=5
        else:
            Pinst=round(25*inst,2)
        Pinst_mean_val=0
        Pinst_std_val=0
        
        #print('Pinst=', Pinst)
                 
     #__________________ Pdividend  Ppayout  Pdividend_____________________    
             
        #print('_________PDividend____________')
        key='Payout'
        
        Ppayout_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Ppayout_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        if self.finviz_df.loc[index,key]==0:
            Ppayout=0
        else:
            Ppayout=intep_3(self.finviz_df.loc[index,key],Ppayout_mean_val,Ppayout_std_val)
     
        
        key='Dividend%'
        divdend=self.finviz_df.loc[index,key]
        Pdividend_mean_val=self.finviz_df[self.finviz_df[key]>0][key].mean(axis=0)
        Pdividend_std_val=self.finviz_df[self.finviz_df[key]>0][key].std(axis=0)
        
        if divdend<=0:  
            Pdivdend=0
        elif divdend>5:
            Pdivdend=5
        else:
            Pdivdend=round(100*divdend,2)
        #print('Pdividend=',Pdivdend)
            
            
    #    print('Proic=',Proic,'; Proa=',Proa,'; Proe=',Proe,'; Pdebt=',Pdebt,
    #          '; Pfcf=',Pfcf,'; Pfpe=',Pfpe,'; Ppe=',Ppe,'; Ppeg=',Ppeg,'; Ppayout=',Ppayout,
    #          '; Pdividend=',Pdivdend,'; Ppricerange=',Ppricerange,'; Prsi=',Prsi,
    #          '; Pshort=',Pshort)
    
        
        
        PHealth=round((Proic+Proa+Proe+Pdebt+Pldebt+Pfcf+Pgrossmargin+Popermargin+Pprofitmargin)/9*20,2)
        PGrowth=round((PEPSQQ+PSaleQQ+PEPSthisY+PEPSNext5Y+PEPSpast5Y+PSalespast5Y+Ppeg)/7*20,2)
        PValue=round((Pfpe+Ppe+Ppb+Pps)/4*20,2)
        PDiv=round((Ppayout+Pdivdend)/2*20,2)
        PTechnical=round((Ppricerange+Prsi+Pshort+Pvol+Pinst+Pinsider+Psma1+Psma2+Psma3)/9*20,2)
        Total=round(2*PHealth+2*PGrowth+PValue+PDiv+PTechnical,2)

        PHealth_mean_val=round(np.mean(PHealth),2)
        PHealth_std_val=round(np.std(PHealth),2)
        PGrowth_mean_val=round(np.mean(PGrowth),2)
        PGrowth_std_val=round(np.std(PGrowth),2)
        PValue_mean_val=round(np.mean(PValue),2)
        PValue_std_val=round(np.std(PValue),2)
        PDiv_mean_val=round(np.mean(PDiv),2)
        PDiv_std_val=round(np.std(PDiv),2)
        PTechnical_mean_val=round(np.mean(PTechnical),2)
        PTechnical_std_val=round(np.std(PTechnical),2)

        
    #    PHealth=round((Proic+Proa+Proe+Pdebt+Pfcf)/5*20,2)
    #    PGrowth=round((Ppeg)/1*20,2)
    #    PValue=round((Pfpe+Ppe+Ppricerange+Prsi+Pshort)/5*20,2)
    #    PDiv=round((Ppayout+Pdivdend)/2*20,2)
    #    Total=round((PHealth+PGrowth+PValue+PDiv)/4,2)
        df1=pd.DataFrame([[PHealth, PGrowth,PValue,PDiv,PTechnical,Total,
                       Proic,Proa,Proe,Pdebt,Pldebt,Pfcf,Pgrossmargin,Popermargin,Pprofitmargin,
                       PEPSQQ,PSaleQQ,PEPSthisY,PEPSNext5Y,PEPSpast5Y,PSalespast5Y,Ppeg,
                       Pfpe,Ppe,Ppb,Pps,
                       Ppayout,Pdivdend,
                       Ppricerange,Prsi,Pshort,Pvol,Pinst,Pinsider,Psma1,Psma2,Psma3]],
        
                  columns=['PHealth', 'PGrowth','PValue','PDiv','Ptechnical','Total',
                       'Proic','Proa','Proe','Pdebt','Pldebt','Pfcf','Pgrossmargin','Popermargin','Pprofitmargin',
                       'PEPSQQ','PSaleQQ','PEPSthisY','PEPSNext5Y','PEPSpast5Y','PSalespast5Y','Ppeg',
                       'Pfpe','Ppe','Ppb','Pps',
                       'Ppayout','Pdivdend',
                       'Ppricerange','Prsi','Pshort','Pvol','Pinst','Pinsider','Psma1','Psma2','Psma3'],
                  index={index})
    
        print('No: ',x, ' :', index, 'Total=', Total, '; PHealth=', PHealth,'; Pgrowth=',PGrowth,'; Pvalue=',PValue,'; PDividend=',PDiv,'; PTechnical=',PTechnical)    
        self.summary=self.summary.append(df1) 
        x=x+1
        #print('_______________________________________________') 
      except: 
            print('Bad data for ticker ', index, '. Xray function skipped for this Symb')
            continue
    Total_mean_val=100
    Total_std_val=100
    df1=pd.DataFrame([[round(PHealth_mean_val), round(PGrowth_mean_val,2),round(PValue_mean_val,2),round(PDiv_mean_val,2),round(PTechnical_mean_val,2),round(Total_mean_val,2),
                       round(Proic_mean_val,2),round(Proa_mean_val,2),round(Proe_mean_val,2),round(Pdebt_mean_val,2),round(Pldebt_mean_val,2),round(Pfcf_mean_val,2),round(Pgrossmargin_mean_val,2),round(Popermargin_mean_val,2),round(Pprofitmargin_mean_val,2),
                       round(PEPSQQ_mean_val,2),round(PSaleQQ_mean_val,2),round(PEPSthisY_mean_val,2),round(PEPSNext5Y_mean_val,2),round(PEPSpast5Y_mean_val,2),round(PSalespast5Y_mean_val,2),round(Ppeg_mean_val,2),
                       round(Pfpe_mean_val,2),round(Ppe_mean_val,2),round(Ppb_mean_val,2),round(Pps_mean_val,2),
                       round(Ppayout_mean_val,2),round(Pdividend_mean_val,2),
                       round(Ppricerange_mean_val,2),round(Prsi_mean_val,2),round(Pshort_mean_val,2),round(Pvol_mean_val,2),round(Pinst_mean_val,2),round(Pinsider_mean_val,2),round(Psma1_mean_val,2),round(Psma2_mean_val,2),round(Psma3_mean_val,2)]],
                columns=['PHealth', 'PGrowth','PValue','PDiv','Ptechnical','Total',
                       'Proic','Proa','Proe','Pdebt','Pldebt','Pfcf','Pgrossmargin','Popermargin','Pprofitmargin',
                       'PEPSQQ','PSaleQQ','PEPSthisY','PEPSNext5Y','PEPSpast5Y','PSalespast5Y','Ppeg',
                       'Pfpe','Ppe','Ppb','Pps',
                       'Ppayout','Pdivdend',
                       'Ppricerange','Prsi','Pshort','Pvol','Pinst','Pinsider','Psma1','Psma2','Psma3'],
                  index={'Mean'})
    self.summary=self.summary.append(df1)
    
    df2=pd.DataFrame([[round(PHealth_std_val), round(PGrowth_std_val,2),round(PValue_std_val,2),round(PDiv_std_val,2),round(PTechnical_std_val,2),round(Total_std_val,2),
                       round(Proic_std_val,2),round(Proa_std_val,2),round(Proe_std_val,2),round(Pdebt_std_val,2),round(Pldebt_std_val,2),round(Pfcf_std_val,2),round(Pgrossmargin_std_val,2),round(Popermargin_std_val,2),round(Pprofitmargin_std_val,2),
                       round(PEPSQQ_std_val,2),round(PSaleQQ_std_val,2),round(PEPSthisY_std_val,2),round(PEPSNext5Y_std_val,2),round(PEPSpast5Y_std_val,2),round(PSalespast5Y_std_val,2),round(Ppeg_std_val,2),
                       round(Pfpe_std_val,2),round(Ppe_std_val,2),round(Ppb_std_val,2),round(Pps_std_val,2),
                       round(Ppayout_std_val,2),round(Pdividend_std_val,2),
                       round(Ppricerange_std_val,2),round(Prsi_std_val,2),round(Pshort_std_val,2),round(Pvol_std_val,2),round(Pinst_std_val,2),round(Pinsider_std_val,2),round(Psma1_std_val,2),round(Psma2_std_val,2),round(Psma3_std_val,2)]],
                  columns=['PHealth', 'PGrowth','PValue','PDiv','Ptechnical','Total',
                       'Proic','Proa','Proe','Pdebt','Pldebt','Pfcf','Pgrossmargin','Popermargin','Pprofitmargin',
                       'PEPSQQ','PSaleQQ','PEPSthisY','PEPSNext5Y','PEPSpast5Y','PSalespast5Y','Ppeg',
                       'Pfpe','Ppe','Ppb','Pps',
                       'Ppayout','Pdivdend',
                       'Ppricerange','Prsi','Pshort','Pvol','Pinst','Pinsider','Psma1','Psma2','Psma3'],
                  index={'STD'})
    self.summary=self.summary.append(df2)
    

def replace_none_with_empty_str(some_list):
    newlist=[]
    for some_dict in some_list:
       some_dict={ k: (0 if v is None else v) for k, v in some_dict.items() }
       newlist.append(some_dict)
    return(newlist)


def intep1(a,b,x):
    if x<a:
        y=0
    elif x>b:
        y=5
    else:
        y=5/(b-a)*x
    return(y)

def intep2(a,b,x):
    if x<a:
        y=5
    elif x>b:
        y=0
    else:
        y=-5/(b-a)*x+5
    return(y)
def intep3(key_val, mean_val,std_val):
    try: 
       n=np.log10(4)/np.log10(1+std_val/mean_val)
    except:
       print('Error in n=log(n)','std_val=',std_val, 'mean_val=',mean_val )
    #print('n=',n)
    if key_val<=0:
        y=0
    else :
        y=round(5-5./(1+(key_val/mean_val)**n),2)
    #print(key,'=',y)
    return(y)

def intep_3(key_val, mean_val,std_val):
    
    n=np.log10(4)/np.log10(1+std_val/mean_val)
    #print('n=',n)
    if key_val==0:
        y=5
    elif key_val<0:
        y=0
    else:
        y=round(5./(1+(key_val/mean_val)**n),2)
    #print(key,'=',y)
    return(y)
    
def intep4(x,a,str1):
    y1=5*(1-1/(1+x**a))
    y=round(2*abs(y1-2.5),2)
    #print(str1,'=',y)
    return(y)
    
    
