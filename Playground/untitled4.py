# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 22:06:02 2018

@author: kuifenhu
"""
from datetime import datetime
import time
from dateutil.relativedelta import relativedelta


from datetime import datetime
ts = int("1284101485")

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))



t=datetime.today()
t=datetime(2018,12,4,17,0,0)

tmp=str(int(time.mktime(t.timetuple())))
print(tmp)