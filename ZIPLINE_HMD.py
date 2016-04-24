# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:56:38 2016

@author: KBS
"""

import pandas_datareader.data as web
import datetime

from zipline.api import  symbol, order_target, set_commission, commission
from zipline.algorithm import TradingAlgorithm


start = datetime.datetime(2015,1,1)
end = datetime.datetime(2016,12,31)

data = web.DataReader('010620.KS','yahoo',start,end)


data = data.tz_localize('UTC')

print(data.head())

def initialize(context):
    set_commission(commission.PerDollar(cost=0.00165))


#==============================================================================
# 어이가 없는게 sym 을 소문자로 하면 안 됨.... ㅡㅡ 정확한건 모르겠음. 확인을 해봐야할 듯.
#==============================================================================
def handle_data(context, data):
    
    sym = symbol('HMD')
    
    order_target(sym,1)


data = data[['Adj Close']]
data.columns = ['HMD']
    

    
algo =TradingAlgorithm(capital_base = 10000000,initialize=initialize, handle_data=handle_data, identifiers=['HMD'])

results = algo.run(data)



#==============================================================================
# print(results.info())
# 
# print(results[['starting_cash','ending_cash','ending_value']])
#==============================================================================
    


#==============================================================================
# print(hmd_aj.head())
#==============================================================================
