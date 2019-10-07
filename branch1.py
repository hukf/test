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
def intep3(x,a):
    y=5-5./(1+x^a)
    return(y)


for x in np.arange(start=0,stop=len(d.finviz_result),step=1):
 #__________________ PHealth  ROI, ROA ROE Debt, FCF,_____________________
   
    roic=d.finviz_result[x]['ROI'][0]
    # curve fitting, <2% =0 >27% =5
    if roic>=0.27:  
        Proic=5
    elif roic<=0.02:
        Proic=0
    else:
        Proic=20*(roic-0.02)
        
        
    roa=d.finviz_result[x]['ROA'][0]
    
    if roa>=0.20:  
        Proa=5
    elif roa<=0:
        Proa=0
    else:
        Proa=round(25*(roa-0),2)
        
    roe=d.finviz_result[x]['ROE'][0]
    
    if roe>=0.40:  
        Proe=5
    elif roe<=0:
        Proe=0
    else:
        Proe=round(12.5*(roe-0),2)
        
        
    debt=d.finviz_result[x]['LTDebt/Eq'][0]
    
    if debt<=0:  
        Pdebt=0
    elif debt>1.4:
        Pdebt=0
    else:
        Pdebt=round(-3.5714*debt+5,2)
    
    fcf=d.finviz_result[x]['P/FCF'][0]
    
    if fcf<=0:  
        Pfcf=0
    elif fcf>64:
        Pfcf=0
    else:
        Pfcf=round(-0.0781*fcf+5,2)
    

    
    #__________________ PGrwoth  PEG_____________________
    peg=d.finviz_result[x]['PEG'][0]
    
    if peg<=0:  
        Ppeg=0
    elif peg>2:
        Ppeg=0
    else:
        Ppeg=round(-0.1471*peg+5,2)
   #[0 2 ] =>[5 0]   
   #'EPSnextQ', 'EPSthisY', 'EPSnext5Y','EPSpast5Y', 'Salespast5Y', 'SalesQ/Q', 'EPSQ/Q', 
#    EPSNextQ=d.finviz_result[x]['EPSnextQ'][0]
#    PEpsNextQ=intep1(0, 0.25,EPSNexQ)
    
    EPSnextY=d.finviz_result[x]['EPSnextY'][0]
    PEpsNextY=intep1(0, 0.25,EPSnextY)
    
#    EPSnext5Y=d.finviz_result[x]['EPSnext5Y'][0]
#    PEpsNext5Y=intep1(0, 0.25,EPSNext5Y)

    EPSthisY=d.finviz_result[x]['EPSthisY'][0]
    PEpsThisY=intep1(0, 0.25,EPSthisY)

    EPSpast5Y=d.finviz_result[x]['EPSpast5Y'][0]
    PEpsPast5Y=intep1(0, 0.25,EPSpast5Y)

    EPSQQ=d.finviz_result[x]['EPSQ/Q'][0]
    PEpsQQ=intep1(0, 0.25,EPSQQ)

    PEpsNext=PEpsNextY+PEpsThisY+PEpsPast5Y+PEpsQQ
    
 #__________________ PValue  Ppe, Pfpe,P/b, P/s, _______________    
 
    fpe=d.finviz_result[x]['ForwardP/E'][0]
    
    if fpe<=0:  
        Pfpe=0
    elif fpe>34:
        Pfpe=0
    else:
        Pfpe=round(-0.1471*fpe+5,2)
     #[0 34 ] =>[5 0]   
    
    pe=d.finviz_result[x]['P/E'][0]
    
    if pe<=0:  
        Ppe=0
    elif pe>34:
        Ppe=0
    else:
        Ppe=round(-0.1471*pe+5,2)
    
    pb=d.finviz_result[x]['P/B'][0]
    Ppb=intep2(2,10,pb)
    
    ps=d.finviz_result[x]['P/S'][0]
    Pps=intep2(1,10,ps)
    
       


 #__________________ PTechnical Ppricerange, Psma1,2,3, Pvol,Prsi,Pshort, Pinst, Pinsider_______    
 
    price=d.finviz_result[x]['Price'][0]
    low=price/(1+d.finviz_result[x]['52WLow'][0])
    high=price/(1+d.finviz_result[x]['52WHigh'][0])
    
    if price<=low:  
        Ppricerange=5
    elif price>high:
        Ppricerange=0
    else:
        k=5/(low-high)
        Ppricerange=round(k*(price-low)+5,2)
        
    sma1=d.finviz_result[x]['SMA20'][0]
    sma2=d.finviz_result[x]['SMA50'][0]
    sma3=d.finviz_result[x]['SMA200'][0]
    
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
        
    
    vol=d.finviz_result[x]['RelVolume'][0]
    
#    if vol<=1:  
#        if vol<0.1:
#            Pvol=5
#        elif vol==0:
#            Pvol=0
#        else:
#           Pvol=round(-5.555*(vol-0.1)+5,2) 
#    elif vol>5:
#        Pvol=5
#    else:
#        Pvol=round(vol,2)
    y=5*(1-1./(1+vol))
    Pvol=round(2*abs(y-2.5),2)
    print(Pvol)
    
    rsi=d.finviz_result[x]['RSI(14)'][0]
    Prsi=round(5-rsi/20,2)

    short=d.finviz_result[x]['ShortFloat'][0]
    
    if short<=0:  
        Pshort=0
    elif short>0.25:
        Pshort=0
    else:
        Pshort=round(-20*short+5,2)
    # range map [0-0.25] to [5:0]
    
    insider=d.finviz_result[x]['InsiderTrans'][0]
    
    if insider<=-0.2:  
        Pinsider=5
    elif insider>0.2:
        Pinsider=5
    else:
        Pinsider=round(25*insider,2)

    inst=d.finviz_result[x]['InstTrans'][0]
    
    if inst<=-0.2:  
        Pinst=-5
    elif short>0.2:
        Pinst=5
    else:
        Pinst=round(25*inst,2)

             
 #__________________ Pdividend  Ppayout  Pdividend_____________________    
         
    payout=d.finviz_result[x]['Payout'][0]
    
    if payout<=0:  
        Ppayout=0
    elif payout>0.9:
        Ppayout=0
    else:
        Ppayout=round(-5.55*payout+5,2)
    
    divdend=d.finviz_result[x]['Dividend%'][0]
    if divdend<=0:  
        Pdivdend=0
    elif divdend>5:
        Pdivdend=5
    else:
        Pdivdend=round(100*divdend,2)
   
        
        
#    print('Proic=',Proic,'; Proa=',Proa,'; Proe=',Proe,'; Pdebt=',Pdebt,
#          '; Pfcf=',Pfcf,'; Pfpe=',Pfpe,'; Ppe=',Ppe,'; Ppeg=',Ppeg,'; Ppayout=',Ppayout,
#          '; Pdividend=',Pdivdend,'; Ppricerange=',Ppricerange,'; Prsi=',Prsi,
#          '; Pshort=',Pshort)

    
    
    PHealth=round(Proic+Proa+Proe+Pdebt+Pfcf,2)
    PGrowth=round(Ppeg+PEpsNext,2)
    PValue=round(Pfpe+Ppe+Ppb+Pps,2)
    PDiv=round(Ppayout+Pdivdend,2)
    PTechnical=round(Ppricerange+Prsi+Pshort+Pvol+Pinst+Pinsider+Psma1+Psma2+Psma3,2)
    Total=round(PHealth+PGrowth+PValue+PDiv+PTechnical,2)
    
#    PHealth=round((Proic+Proa+Proe+Pdebt+Pfcf)/5*20,2)
#    PGrowth=round((Ppeg)/1*20,2)
#    PValue=round((Pfpe+Ppe+Ppricerange+Prsi+Pshort)/5*20,2)
#    PDiv=round((Ppayout+Pdivdend)/2*20,2)
#    Total=round((PHealth+PGrowth+PValue+PDiv)/4,2)
    
    df1=pd.DataFrame([[PHealth, PGrowth,PValue,PDiv,PTechnical,Total]],columns=['PHealth', 'PGrowth','PValue','PDiv','Ptechnical','Total'],index={d.finviz_result[x]['symb'][0]})
    print(d.finviz_result[x]['symb'][0], 'Total=', Total, '; PHealth=', PHealth,'; Pgrowth=',PGrowth,'; Pvalue=',PValue,'; PDividend=',PDiv,'; PTechnical=',PTechnical)    
    df=df.append(df1) 




df.mean(axis=0)
df.sort_values(by=['Total'])


