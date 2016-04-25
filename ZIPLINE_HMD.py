# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:56:38 2016

@author: KBS
"""

import pandas_datareader.data as web
import datetime

from zipline.api import  symbol, order_target, set_commission, commission, add_history, history, record
from zipline.algorithm import TradingAlgorithm


start = datetime.datetime(2015,1,1)
end = datetime.datetime(2016,12,31)

data = web.DataReader('AAPL','yahoo',start,end)

print(data)

data = data.tz_localize('UTC')


def initialize(context):
    set_commission(commission.PerDollar(cost=0.00165))
    add_history(5, '1d', 'price')
    add_history(20, '1d', 'price')
    context.i = 0
    context.investment = False

#==============================================================================
# 어이가 없는게 sym 을 소문자로 하면 안 됨.... ㅡㅡ 정확한건 모르겠음. 확인을 해봐야할 듯.
#==============================================================================
def handle_data(context, data):
    
    context.i += 1
    if context.i < 20:    
        return
        
    ma5 = history(5,'1d','price').mean()
    ma20 = history(20, '1d', 'price').mean()
    buy = False
    sell = False
    
    sym = symbol('HMD')
    if ma5[sym] > ma20[sym] and context.investment == False:
        order_target(sym, 1)
        context.investment = True
        buy = True

    elif ma5[sym] < ma20[sym] and context.investment == True:
        order_target(sym, -1)
        context.investment = False
        sell = True
        
    record(HMD=data[sym].price, ma5=ma5[sym], ma20=ma20[sym], buy=buy, sell=sell)

            
    
        
#==============================================================================
#     sym = symbol('HMD')
#     
#     order_target(sym,1)
#==============================================================================


data = data[['Adj Close']]

data.columns = ['HMD']

    

    
algo =TradingAlgorithm(capital_base = 10000000,initialize=initialize, handle_data=handle_data, identifiers=['HMD'])

results = algo.run(data)


print(results.info())
print(results.buy)

ax = results[['ma5','ma20']].plot(figsize=(16,4))
ax.plot(results.ix[results.buy == True].index, results.ma5[results.buy == True],'^')
ax.plot(results.ix[results.sell == True].index, results.ma5[results.sell == True],'^')
results['ending_cash'].plot(figsize=(16,4),secondary_y=True)


#==============================================================================
# results['portfolio_value'].plot()
#==============================================================================

#==============================================================================
# print(results.info())
# 
# print(results[['starting_cash','ending_cash','ending_value']])
#==============================================================================
    


#==============================================================================
# print(hmd_aj.head())
#==============================================================================
