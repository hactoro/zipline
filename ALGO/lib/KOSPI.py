# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:19:27 2016

@author: KBS
"""

import pandas as pd
import pandas_datareader.data as pdr



## Get AdjustClose set from yahoo finance
## input : kospi symbol list, date
## output : kospi adjust close dataframe
def GetAdjustClose(lSymbol, start, end):
    
    ldf = []
    for item in lSymbol:
        ldf.append(pdr.DataReader(item, 'yahoo', start, end)['Adj Close'])
        

    df = pd.concat(ldf, axis=1)
    
    return df