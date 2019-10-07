# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:18:08 2019

@author: kuifenhu
"""
import numpy as np
df=pd.DataFrame()
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
    n=np.log10(4)/np.log10(1+std_val/mean_val)
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
    if key_val<0:
        y=5
    elif key_val==0 :
        y=0
    else:
        y=round(5./(1+(key_val/mean_val)**n),2)
    #print(key,'=',y)
    return(y)
    
def intep4(x,a,str1):
    y1=5*(1-1/(1+x**a))
    y=round(2*abs(y1-2.5),2)
    print(str1,'=',y)
    return(y)
    
    
# convert the finviz_result into dataframe    
d.finviz_df=pd.DataFrame()
df=pd.DataFrame()
x=0

for x in np.arange(start=0,stop=len(d.finviz_result),step=1):
    d.finviz_df=d.finviz_df.append(d.finviz_result[x])
d.finviz_df=d.finviz_df.set_index('symb')

# calculate the mean and standard diviation 


# calcuate the normaized key matrix
    
#for x in np.arange(start=0,stop=len(d.finviz_result),step=1):
for index, row in d.finviz_df.iterrows():
    print(index)
#__________________ PHealth  ROI, ROA ROE Debt, FCF,_____________________
   
    print('_________PHealth____________')  
    key='ROA'
    mean_val=d.finviz_df[d.finviz_df[key]>0].mean(axis=0)
    std_val=d.finviz_df[d.finviz_df[key]>0].std(axis=0)
    Proa=intep3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])
        
    key='ROE'
    Proe=intep3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])
    
    key='ROI'
    Proic=intep3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])
    
    key='P/FCF'
    Pfcf=intep_3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])

    key='LTDebt/Eq'
    Pldebt=intep_3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])

    key='Debt/Eq'
    Pdebt=intep_3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])
  
 #__________________ PValue  Ppe, Pfpe,P/b, P/s, _______________    
 
    print('_________PValue____________')
    
    key='ForwardP/E'
    Pfpe=intep_3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])

    key='P/E'
    Ppe=intep_3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])

    key='P/B'
    Ppb=intep_3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])

    key='P/S'
    Pps=intep_3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])

       
#__________________ PGrwoth  PEG_____________________
    
    print('_________PGrowth____________')

    key='PEG'
    Ppeg=intep_3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])
    
    EPSNextQ=d.finviz_result[x]['EPSnextQ'][0]
    PEpsNextQ=intep1(0, 0.25,EPSNexQ)
    
    EPSnextY=d.finviz_result[x]['EPSnextY'][0]
    PEpsNextY=intep3(EPSnextY/0.125,2,'EPSnextY%')
    

    key='EPSQ/Q'
    PEpsQQ=intep3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])

    key='SalesQ/Q'
    PSaleQQ=intep3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])

    key='EPSthisY'
    PEpsThisY=intep3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])

    key='EPSnext5Y'
    PEpsNext5Y=intep3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])
    
#    EPSpast5Y=d.finviz_result[x]['EPSpast5Y'][0]
#    PEpsPast5Y=intep_3(EPSpast5Y/0.125,1,'EPSpast5Y')
    
    PEpsNext=PEpsQQ*0.2+PSaleQQ*0.2+PEpsNext5Y*0.2+Ppeg*0.2+0.2*PEpsThisY




 #__________________ PTechnical Ppricerange, Psma1,2,3, Pvol,Prsi,Pshort, Pinst, Pinsider_______    
 
    print('_________PTechnical____________')
    price=d.finviz_df.loc[index,'Price']
    low=price/(1+d.finviz_df.loc[index,'52WLow'])
    high=price/(1+d.finviz_df.loc[index,'52WHigh'])
    
    if price<=low:  
        Ppricerange=5
    elif price>high:
        Ppricerange=0
    else:
        k=5/(low-high)
        Ppricerange=round(k*(price-low)+5,2)
    print('Ppricerange=',Ppricerange)  
    
    sma1=d.finviz_df.loc[index,'SMA20']
    sma2=d.finviz_df.loc[index,'SMA50']
    sma3=d.finviz_df.loc[index,'SMA200']
    
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
    print('sma20=',Psma1,'sma50=',Psma2,'sma200=',Psma3)    
    
    vol=d.finviz_df.loc[index,'RelVolume']
    Pvol=intep4(vol,1,'RelVolulm')
    
    rsi=d.finviz_df.loc[index,'RSI(14)']
    Prsi=round(5-rsi/20,2)
    print('Prsi=', rsi)

    key='ShortFloat'
    Pshort=intep3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])
  
    # range map [0-0.25] to [5:0]
    
    insider=d.finviz_df.loc[index,'InsiderTrans']
    
    if insider<=-0.2:  
        Pinsider=5
    elif insider>0.2:
        Pinsider=5
    else:
        Pinsider=round(25*insider,2)
    print('Pinsider=', Pinsider)
    
    inst=d.finviz_df.loc[index,'InstTrans']
    
    if inst<=-0.2:  
        Pinst=-5
    elif short>0.2:
        Pinst=5
    else:
        Pinst=round(25*inst,2)
    print('Pinst=', Pinst)
             
 #__________________ Pdividend  Ppayout  Pdividend_____________________    
         
    print('_________PDividend____________')
    key='Payout'
    Ppayout=intep3(d.finviz_df.loc[index,key],mean_val[key],std_val[key])
 
    
    divdend=d.finviz_df.loc[index,'Dividend%']
    if divdend<=0:  
        Pdivdend=0
    elif divdend>5:
        Pdivdend=5
    else:
        Pdivdend=round(100*divdend,2)
    print('Pdividend=',Pdivdend)
        
        
#    print('Proic=',Proic,'; Proa=',Proa,'; Proe=',Proe,'; Pdebt=',Pdebt,
#          '; Pfcf=',Pfcf,'; Pfpe=',Pfpe,'; Ppe=',Ppe,'; Ppeg=',Ppeg,'; Ppayout=',Ppayout,
#          '; Pdividend=',Pdivdend,'; Ppricerange=',Ppricerange,'; Prsi=',Prsi,
#          '; Pshort=',Pshort)

    
    
    PHealth=round((Proic+Proa+Proe+Pdebt+Pldebt+Pfcf)/6*20,2)
    PGrowth=round((PEpsNext)*20,2)
    PValue=round((Pfpe+Ppe+Ppb+Pps)/4*20,2)
    PDiv=round((Ppayout+Pdivdend)/2*20,2)
    PTechnical=round((Ppricerange+Prsi+Pshort+Pvol+Pinst+Pinsider+Psma1+Psma2+Psma3)/9*20,2)
    Total=round(PHealth+PGrowth+PValue+PDiv+PTechnical,2)
    
#    PHealth=round((Proic+Proa+Proe+Pdebt+Pfcf)/5*20,2)
#    PGrowth=round((Ppeg)/1*20,2)
#    PValue=round((Pfpe+Ppe+Ppricerange+Prsi+Pshort)/5*20,2)
#    PDiv=round((Ppayout+Pdivdend)/2*20,2)
#    Total=round((PHealth+PGrowth+PValue+PDiv)/4,2)
    
    df1=pd.DataFrame([[PHealth, PGrowth,PValue,PDiv,PTechnical,Total,
                       Proic,Proa,Proe,Pdebt,Pldebt,Pfcf,
                       PEpsNex,
                       Pfpe,Ppe,Ppb,Pps,
                       Ppayout,Pdivdend,
                       Ppricerange,Prsi,Pshort,Pvol,Pinst,Pinsider,Psma1,Psma2,Psma3]],
                  columns=['PHealth', 'PGrowth','PValue','PDiv','Ptechnical','Total',
                       'Proic','Proa','Proe','Pdebt','Pldebt','Pfcf',
                       'PEpsNex',
                       'Pfpe','Ppe','Ppb','Pps',
                       'Ppayout','Pdivdend',
                       'Ppricerange','Prsi','Pshort','Pvol','Pinst','Pinsider','Psma1','Psma2','Psma3'],
                  index={index})
    
    print('No: ',x, ' :', index, 'Total=', Total, '; PHealth=', PHealth,'; Pgrowth=',PGrowth,'; Pvalue=',PValue,'; PDividend=',PDiv,'; PTechnical=',PTechnical)    
    df=df.append(df1) 
    x=x+1
    print('_______________________________________________')



df.mean(axis=0)
df.sort_values(by=['Total'],ascending=False)


