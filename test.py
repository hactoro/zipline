# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 22:27:03 2016

@author: KBS
"""

import zipline
from zipline.api import order_target, order, symbol, history, add_history, record

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2015,1,1)

data = web.DataReader('AAPL','yahoo',start,end)
#==============================================================================
# data['Adj Close'].plot(figsize=(16,4))
#==============================================================================


def initialize(context):
    add_history(5, '1d', 'price')
    add_history(20, '1d', 'price')
    context.i = 0
    


def handle_data(context, data):
    context.i += 1
    if context.i < 20:
        return
        
    ma5 = history(5, '1d', 'price').mean()
    ma20 = history(20, '1d', 'price').mean()
    buy = False
    sell = False    
    
    
    sym = symbol('AAPL')
    if ma5[sym] > ma20[sym]:
        order_target(sym, 1)
        buy = True
    else:
        order_target(sym, -1)
        sell = True
    
    record(AAPL=data[sym].price, ma5=ma5[sym], ma20=ma20[sym], buy=buy, sell=sell)
    
    
  
    
    
    
    
data = data[['Adj Close']]

data.columns = ['AAPL']


data = data.tz_localize('UTC')


from zipline.algorithm import TradingAlgorithm
algo = TradingAlgorithm(capital_base =100000000, initialize=initialize, handle_data=handle_data, identifiers=['AAPL'])

results = algo.run(data)


results.portfolio_value.plot(figsize=(16,4))




#==============================================================================
# print(results.head())
# 
# print(results.portfolio_value)
# 
# #==============================================================================
#==============================================================================
# print(results['portfolio_value'])
#==============================================================================

#==============================================================================
# results['portfolio_value'].plot()
#==============================================================================
