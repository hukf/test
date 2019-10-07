# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:22:09 2018

@author: kuifenhu
"""
import talib as ta

import matplotlib.pyplot as plt
import numpy as np

class TaObj:
  def __init__(self):
        #self.d=d
        self.inputdata=[]
        self.output=[]
        self.ema=[]
        self.sma=[]
        self.tp=14
        self.tp1=50
        self.tp2=500
        

      
  def calculate(self,para):

    self.t=self.inputdata[:,0]
    self.op=self.inputdata[:,1]
    self.high=self.inputdata[:,2]
    self.low=self.inputdata[:,3]
    self.close=self.inputdata[:,4]
    #adjusted close 
    self.close1=self.inputdata[:,5]
    self.volume=self.inputdata[:,6]
    #Overlap study
     
    #Overlap Studies
    #Overlap Studies
    if para is 'BBANDS'               : #Bollinger Bands
        upperband, middleband, lowerband = ta.BBANDS(self.close, timeperiod=self.tp, nbdevup=2, nbdevdn=2, matype=0)
        self.output=[upperband, middleband, lowerband]
        
    elif para is 'DEMA'                 : #Double Exponential Moving Average
        self.output = ta.DEMA(self.close, timeperiod=self.tp)
        
    elif para is 'EMA'                  : #Exponential Moving Average
        self.output = ta.EMA(self.close, timeperiod=self.tp)
        
    elif para is 'HT_TRENDLINE'         : #Hilbert Transform - Instantaneous Trendline
        self.output = ta.HT_TRENDLINE(self.close)
        
    elif para is 'KAMA'                 : #Kaufman Adaptive Moving Average
        self.output = ta.KAMA(self.close, timeperiod=self.tp)
        
    elif para is 'MA'                   : #Moving average
        self.output = ta.MA(self.close, timeperiod=self.tp, matype=0)
        
    elif para is 'MAMA'                 : #MESA Adaptive Moving Average
        mama, fama = ta.MAMA(self.close, fastlimit=0, slowlimit=0)
        
    elif para is 'MAVP'                 : #Moving average with variable period
        self.output = ta.MAVP(self.close, periods=10, minperiod=self.tp, maxperiod=self.tp1, matype=0)
        
    elif para is 'MIDPOINT'             : #MidPoint over period
        self.output = ta.MIDPOINT(self.close, timeperiod=self.tp)
        
    elif para is 'MIDPRICE'             : #Midpoint Price over period
        self.output = ta.MIDPRICE(self.high, self.low, timeperiod=self.tp)
        
    elif para is 'SAR'                  : #Parabolic SAR
        self.output = ta.SAR(self.high, self.low, acceleration=0, maximum=0)
        
    elif para is 'SAREXT'               : #Parabolic SAR - Extended
        self.output = ta.SAREXT(self.high, self.low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
        
    elif para is 'SMA'                  : #Simple Moving Average
        self.output = ta.SMA(self.close, timeperiod=self.tp)
        
    elif para is 'T3'                   : #Triple Exponential Moving Average (T3)
        self.output = ta.T3(self.close, timeperiod=self.tp, vfactor=0)
        
    elif para is 'TEMA'                 : #Triple Exponential Moving Average
        self.output = ta.TEMA(self.close, timeperiod=self.tp)
        
    elif para is 'TRIMA'                : #Triangular Moving Average
        self.output = ta.TRIMA(self.close, timeperiod=self.tp)
        
    elif para is 'WMA'                  : #Weighted Moving Average
        self.output = ta.WMA(self.close, timeperiod=self.tp)
        
      
    #Momentum Indicators
    elif para is 'ADX'                  : #Average Directional Movement Index
        self.output = ta.ADX(self.high, self.low, self.close, timeperiod=self.tp)
        
    elif para is 'ADXR'                 : #Average Directional Movement Index Rating
        self.output = ta.ADXR(self.high, self.low, self.close, timeperiod=self.tp)
        
    elif para is 'APO'                  : #Absolute Price Oscillator
        self.output = ta.APO(self.close, fastperiod=12, slowperiod=26, matype=0)
         
    elif para is 'AROON'                : #Aroon
        aroondown, aroonup = ta.AROON(self.high, self.low, timeperiod=self.tp)
        self.output=[aroondown, aroonup]
    
    elif para is 'AROONOSC'             : #Aroon Oscillator
        self.output = ta.AROONOSC(self.high, self.low, timeperiod=self.tp) 
        
    elif para is 'BOP'                  : #Balance Of Power
        self.output = ta.BOP(self.op, self.high, self.low, self.close)
         
    elif para is 'CCI'                  : #Commodity Channel Index
        self.output = ta.CCI(self.high, self.low, self.close, timeperiod=self.tp)
         
    elif para is 'CMO'                  : #Chande Momentum Oscillator
        self.output = ta.CMO(self.close, timeperiod=self.tp)
         
    elif para is 'DX'                   : #Directional Movement Index
        self.output = ta.DX(self.high, self.low, self.close, timeperiod=self.tp)
         
    elif para is 'MACD'                 : #Moving Average Convergence/Divergence
        macd, macdsignal, macdhist = ta.MACD(self.close, fastperiod=12, slowperiod=26, signalperiod=9)
        self.output=[macd, macdsignal, macdhist]
    elif para is 'MACDEXT'              : #MACD with controllable MA type
        macd, macdsignal, macdhist = ta.MACDEXT(self.close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
        self.output=[macd, macdsignal, macdhist]
    elif para is 'MACDFIX'              : #Moving Average Convergence/Divergence Fix 12/26
        macd, macdsignal, macdhist = ta.MACDFIX(self.close, signalperiod=9)
        self.output=[macd, macdsignal, macdhist]
    elif para is 'MFI'                  : #Money Flow Index
        self.output = ta.MFI(self.high, self.low, self.close, self.volume, timeperiod=self.tp)
         
    elif para is 'MINUS_DI'             : #Minus Directional Indicator
        self.output = ta.MINUS_DI(self.high, self.low, self.close, timeperiod=self.tp)
         
    elif para is 'MINUS_DM'             : #Minus Directional Movement
        self.output = ta.MINUS_DM(self.high, self.low, timeperiod=self.tp)
         
    elif para is 'MOM'                  : #Momentum
        self.output = ta.MOM(self.close, timeperiod=10)
         
    elif para is 'PLUS_DI'              : #Plus Directional Indicator
        self.output = ta.PLUS_DI(self.high, self.low, self.close, timeperiod=self.tp)
         
    elif para is 'PLUS_DM'              : #Plus Directional Movement
        self.output = ta.PLUS_DM(self.high, self.low, timeperiod=self.tp)
         
    elif para is 'PPO'                  : #Percentage Price Oscillator
        self.output = ta.PPO(self.close, fastperiod=12, slowperiod=26, matype=0)
         
    elif para is 'ROC'                  : #Rate of change : ((price/prevPrice)-1)*100
        self.output = ta.ROC(self.close, timeperiod=10)
         
    elif para is 'ROCP'                 : #Rate of change Percentage: (price-prevPrice)/prevPrice
        self.output = ta.ROCP(self.close, timeperiod=10)
         
    elif para is 'ROCR'                 : #Rate of change ratio: (price/prevPrice)
        self.output = ta.ROCR(self.close, timeperiod=10)
         
    elif para is 'ROCR100'              : #Rate of change ratio 100 scale: (price/prevPrice)*100
        self.output = ta.ROCR100(self.close, timeperiod=10)
         
    elif para is 'RSI'                  : #Relative Strength Index
        self.output = ta.RSI(self.close, timeperiod=self.tp)
         
    elif para is 'STOCH'                : #Stochastic
        slowk, slowd = ta.STOCH(self.high, self.low, self.close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3,slowd_matype=0)
        self.output=[slowk, slowd]
		
    elif para is 'STOCHF'               : #Stochastic Fast
        fastk, fastd = ta.STOCHF(self.high, self.low, self.close, fastk_period=5, fastd_period=3, fastd_matype=0)
        self.output=[fastk, fastd]
		
    elif para is 'STOCHRSI'             : #Stochastic Relative Strength Index
        fastk, fastd = ta.STOCHRSI(self.close, timeperiod=self.tp, fastk_period=5, fastd_period=3, fastd_matype=0)
        self.output=[fastk, fastd]
		
    elif para is 'TRIX'                 : #1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
        self.output = ta.TRIX(self.close, timeperiod=self.tp)
         
		
    elif para is 'ULTOSC'               : #Ultimate Oscillator
        self.output = ta.ULTOSC(self.high, self.low, self.close, timeperiod1=self.tp, timeperiod2=self.tp1, timeperiod3=self.tp2)
         
		
    elif para is 'WILLR'                : #Williams' %R
        self.output = ta.WILLR(self.high, self.low, self.close, timeperiod=self.tp)
         

    # Volume Indicators    : #
    elif para is 'AD'                   : #Chaikin A/D Line
        self.output = ta.AD(self.high, self.low, self.close, self.volume)
        
    elif para is 'ADOSC'                : #Chaikin A/D Oscillator
        self.output = ta.ADOSC(self.high, self.low, self.close, self.volume, fastperiod=3, slowperiod=10)
        
    elif para is 'OBV'                  : #On Balance Volume
        self.output = ta.OBV(self.close, self.volume)
        
        
   # Volatility Indicators: #
    elif para is 'ATR'                  : #Average True Range
        self.output = ta.ATR(self.high, self.low, self.close, timeperiod=self.tp)
         
    elif para is 'NATR'                 : #Normalized Average True Range
        self.output = ta.NATR(self.high, self.low, self.close, timeperiod=self.tp)
         
    elif para is 'TRANGE'               : #True Range
        self.output = ta.TRANGE(self.high, self.low, self.close)
         
    
    #Price Transform      : #
    elif para is 'AVGPRICE'             : #Average Price
        self.output = ta.AVGPRICE(self.op, self.high, self.low, self.close)
         
    elif para is 'MEDPRICE'             : #Median Price
        self.output = ta.MEDPRICE(self.high, self.low)
         
    elif para is 'TYPPRICE'             : #Typical Price
        self.output = ta.TYPPRICE(self.high, self.low, self.close)
         
    elif para is 'WCLPRICE'             : #Weighted Close Price
        self.output = ta.WCLPRICE(self.high, self.low, self.close)
         
    #Cycle Indicators     : #
    elif para is 'HT_DCPERIOD'          : #Hilbert Transform - Dominant Cycle Period
        self.output = ta.HT_DCPERIOD(self.close)
         
    elif para is 'HT_DCPHASE'           : #Hilbert Transform - Dominant Cycle Phase
        self.output = ta.HT_DCPHASE(self.close)
         
    elif para is 'HT_PHASOR'            : #Hilbert Transform - Phasor Components
        inphase, quadrature = ta.HT_PHASOR(self.close)
        self.output=[inphase, quadrature]
		
    elif para is 'HT_SINE'              : #Hilbert Transform - SineWave #2
        sine, leadsine = ta.HT_SINE(self.close)
        self.output=[sine, leadsine]
         
        
    elif para is 'HT_TRENDMODE'         : #Hilbert Transform - Trend vs Cycle Mode
        self.integer = ta.HT_TRENDMODE(self.close)
         
        
    #Pattern Recognition  : #
    elif para is 'CDL2CROWS'            : #Two Crows
        self.integer = ta.CDL2CROWS(self.op, self.high, self.low, self.close)
         
    elif para is 'CDL3BLACKCROWS'       : #Three Black Crows
        self.integer = ta.CDL3BLACKCROWS(self.op, self.high, self.low, self.close)
        
    elif para is 'CDL3INSIDE'           : #Three Inside Up/Down
        self.integer = ta.CDL3INSIDE(self.op, self.high, self.low, self.close)
        
    elif para is 'CDL3LINESTRIKE'       : #Three-Line Strike
        self.integer = ta.CDL3LINESTRIKE(self.op, self.high, self.low, self.close)
        
    elif para is 'CDL3OUTSIDE'          : #Three Outside Up/Down
        self.integer = ta.CDL3OUTSIDE(self.op, self.high, self.low, self.close)
        
    elif para is 'CDL3STARSINSOUTH'     : #Three Stars In The South
        self.integer = ta.CDL3STARSINSOUTH(self.op, self.high, self.low, self.close)
        
    elif para is 'CDL3WHITESOLDIERS'    : #Three Advancing White Soldiers
        self.integer = ta.CDL3WHITESOLDIERS(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLABANDONEDBABY'     : #Abandoned Baby
        self.integer = ta.CDLABANDONEDBABY(self.op, self.high, self.low, self.close, penetration=0)
        
    elif para is 'CDLBELTHOLD'          : #Belt-hold
        self.integer = ta.CDLBELTHOLD(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLBREAKAWAY'         : #Breakaway
        self.integer = ta.CDLBREAKAWAY(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLCLOSINGMARUBOZU'   : #Closing Marubozu
        self.integer = ta.CDLCLOSINGMARUBOZU(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLCONCEALBABYSWALL'  : #Concealing Baby Swallow
        self.integer = ta.CDLCONCEALBABYSWALL(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLCOUNTERATTACK'     : #Counterattack
        self.integer = ta.CDLCOUNTERATTACK(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLDARKCLOUDCOVER'    : #Dark Cloud Cover
        self.integer = ta.CDLDARKCLOUDCOVER(self.op, self.high, self.low, self.close, penetration=0)
        
    elif para is 'CDLDOJI'              : #Doji
        self.integer = ta.CDLDOJI(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLDOJISTAR'          : #Doji Star
        self.integer = ta.CDLDOJISTAR(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLDRAGONFLYDOJI'     : #Dragonfly Doji
        self.integer = ta.CDLDRAGONFLYDOJI(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLENGULFING'         : #Engulfing Pattern
        self.integer = ta.CDLENGULFING(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLEVENINGDOJISTAR'   : #Evening Doji Star
        self.integer = ta.CDLEVENINGDOJISTAR(self.op, self.high, self.low, self.close, penetration=0)
        
    elif para is 'CDLEVENINGSTAR'       : #Evening Star
        self.integer = ta.CDLEVENINGSTAR(self.op, self.high, self.low, self.close, penetration=0)
        
    elif para is 'CDLGAPSIDESIDEWHITE'  : #Up/Down-gap side-by-side white lines
        self.integer = ta.CDLGAPSIDESIDEWHITE(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLGRAVESTONEDOJI'    : #Gravestone Doji
        self.integer = ta.CDLGRAVESTONEDOJI(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLHAMMER'            : #Hammer
        self.integer = ta.CDLHAMMER(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLHANGINGMAN'        : #Hanging Man
        self.integer = ta.CDLHANGINGMAN(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLHARAMI'            : #Harami Pattern
        self.integer = ta.CDLHARAMI(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLHARAMICROSS'       : #Harami Cross Pattern
        self.integer = ta.CDLHARAMICROSS(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLHIGHWAVE'          : #High-Wave Candle
        self.integer = ta.CDLHIGHWAVE(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLHIKKAKE'           : #Hikkake Pattern
        self.integer = ta.CDLHIKKAKE(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLHIKKAKEMOD'        : #Modified Hikkake Pattern
        self.integer = ta.CDLHIKKAKEMOD(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLHOMINGPIGEON'      : #Homing Pigeon
        self.integer = ta.CDLHOMINGPIGEON(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLIDENTICAL3CROWS'   : #Identical Three Crows
        self.integer = ta.CDLIDENTICAL3CROWS(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLINNECK'            : #In-Neck Pattern
        self.integer = ta.CDLINNECK(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLINVERTEDHAMMER'    : #Inverted Hammer
        self.integer = ta.CDLINVERTEDHAMMER(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLKICKING'           : #Kicking
        self.integer = ta.CDLKICKING(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLKICKINGBYLENGTH'   : #Kicking - bull/bear determined by the longer marubozu
        self.integer = ta.CDLKICKINGBYLENGTH(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLLADDERBOTTOM'      : #Ladder Bottom
        self.integer = ta.CDLLADDERBOTTOM(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLLONGLEGGEDDOJI'    : #Long Legged Doji
        self.integer = ta.CDLLONGLEGGEDDOJI(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLLONGLINE'          : #Long Line Candle
        self.integer = ta.CDLLONGLINE(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLMARUBOZU'          : #Marubozu
        self.integer = ta.CDLMARUBOZU(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLMATCHINGLOW'      : #Matching Low
        self.integer = ta.CDLMATCHINGLOW(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLMATHOLD'           : #Mat Hold
        self.integer = ta.CDLMATHOLD(self.op, self.high, self.low, self.close, penetration=0)
        
    elif para is 'CDLMORNINGDOJISTAR'   : #Morning Doji Star
        self.integer = ta.CDLMORNINGDOJISTAR(self.op, self.high, self.low, self.close, penetration=0)
        
    elif para is 'CDLMORNINGSTAR'       : #Morning Star
        self.integer = ta.CDLMORNINGSTAR(self.op, self.high, self.low, self.close, penetration=0)
        
    elif para is 'CDLONNECK'            : #On-Neck Pattern
        self.integer = ta.CDLONNECK(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLPIERCING'          : #Piercing Pattern
        self.integer = ta.CDLPIERCING(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLRICKSHAWMAN'       : #Rickshaw Man
        self.integer = ta.CDLRICKSHAWMAN(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLRISEFALL3METHODS'  : #Rising/Falling Three Methods
        self.integer = ta.CDLRISEFALL3METHODS(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLSEPARATINGLINES'   : #Separating Lines
        self.integer = ta.CDLSEPARATINGLINES(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLSHOOTINGSTAR'      : #Shooting Star
        self.integer = ta.CDLSHOOTINGSTAR(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLSHORTLINE'         : #Short Line Candle
        self.integer = ta.CDLSHORTLINE(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLSPINNINGTOP'       : #Spinning Top
        self.integer = ta.CDLSPINNINGTOP(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLSTALLEDPATTERN'    : #Stalled Pattern
        self.integer = ta.CDLSTALLEDPATTERN(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLSTICKSANDWICH'     : #Stick Sandwich
        self.integer = ta.CDLSTICKSANDWICH(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLTAKURI'            : #Takuri (Dragonfly Doji with very long lower shadow)
        self.integer = ta.CDLTAKURI(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLTASUKIGAP'         : #Tasuki Gap
        self.integer = ta.CDLTASUKIGAP(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLTHRUSTING'         : #Thrusting Pattern
        self.integer = ta.CDLTHRUSTING(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLTRISTAR'           : #Tristar Pattern
        self.integer = ta.CDLTRISTAR(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLUNIQUE3RIVER'      : #Unique 3 River
        self.integer = ta.CDLUNIQUE3RIVER(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLUPSIDEGAP2CROWS'   : #Upside Gap Two Crows
        self.integer = ta.CDLUPSIDEGAP2CROWS(self.op, self.high, self.low, self.close)
        
    elif para is 'CDLXSIDEGAP3METHODS'  : #Upside/Downside Gap Three Methods
        self.integer = ta.CDLXSIDEGAP3METHODS(self.op, self.high, self.low, self.close)
        
     
     #Statistic Functions  : #
    elif para is 'BETA'                 : #Beta
        self.output = ta.BETA(self.high, self.low, timeperiod=5)
         
    elif para is 'CORREL'               : #Pearson's Correlation Coefficient (r)
        self.output = ta.CORREL(self.high, self.low, timeperiod=self.tp)
         
    elif para is 'LINEARREG'            : #Linear Regression
        self.output = ta.LINEARREG(self.close, timeperiod=self.tp)
         
    elif para is 'LINEARREG_ANGLE'      : #Linear Regression Angle
        self.output = ta.LINEARREG_ANGLE(self.close, timeperiod=self.tp)
         
    elif para is 'LINEARREG_INTERCEPT'  : #Linear Regression Intercept
        self.output = ta.LINEARREG_INTERCEPT(self.close, timeperiod=self.tp)
         
    elif para is 'LINEARREG_SLOPE'      : #Linear Regression Slope
        self.output = ta.LINEARREG_SLOPE(self.close, timeperiod=self.tp)
        
    elif para is 'STDDEV'               : #Standard Deviation
        self.output = ta.STDDEV(self.close, timeperiod=5, nbdev=1)
        
    elif para is 'TSF'                  : #Time Series Forecast
        self.output = ta.TSF(self.close, timeperiod=self.tp)
        
    elif para is 'VAR'                  : #Variance
        self.output = ta.VAR(self.close, timeperiod=5, nbdev=1)
        
    else:
        print('You issued command:' +para)

    
#      l1,=plt.plot(self.t,ta.SMA(data[:,4],timeperiod=10),label="sma10",gid='sma10')
#      l2,=plt.plot(self.t,ta.SMA(data[:,4],timeperiod=50),label="sma50",gid='sma50')
#      l3,=plt.plot(self.t,ta.SMA(data[:,4],timeperiod=200),label="sma200",gid='sma200')




#   elif para is 'AD'                   : #Chaikin A/D Line
#        self.output = ta.AD(self.high, self.low, self.close, self.volume)
#        l1,=plt.plot(self.t,self.output,label="AD")
#        self.AD.append(l1)
#    elif para is 'ADOSC'                : #Chaikin A/D Oscillator
#        self.output = ta.ADOSC(s:lf.high, self.low, self.close, self.volume, fastperiod=3, slowperiod=10)
#        l1,=plt.plot(self.t,self.output,label="ADOSC")
#        self.ADOSC.append(l1)
#    elif para is 'OBV'                  : #On Balance Volume
#        self.output = ta.OBV(self.close, self.volume)
#        l1,=plt.plot(self.t,self.output,label="OBV")
#        self.OBV.append(l1)
#   # Volatility Indicators: #
#    elif para is 'ATR'                  : #Average True Range
#        self.output = ta.ATR(self.high, self.low, self.close, timeperiod=self.tp)
#        l1,=plt.plot(self.t,self.output,label="ATR")
#        self.ATR.append(l1)
#    elif para is 'NATR'                 : #Normalized Average True Range
#        self.output = ta.NATR(self.high, self.low, self.close, timeperiod=self.tp)
#        l1,=plt.plot(self.t,self.output,label="NATR")
#        self.NATR.append(l1)
#    elif para is 'TRANGE'               : #True Range
#        self.output = ta.TRANGE(self.high, self.low, self.close)
#        l1,=plt.plot(self.t,self.output,label="TRANGE")
#        self.TRANGE.append(l1)
        





      