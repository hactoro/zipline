# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:19:57 2016

@author: KBS
"""

## PAIR TRADING 확인해보기.
## 관계성이 높은 그룹사. 현대중공업과 현대미포조선을 통해 PAIR TRADING 이익성을 확인해보기..

## 정규화.
def normalize(df):
    
    normDF = (df-df.mean())/(df.max()-df.min())
    
    return normDF    


import pandas as pd
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2015,12,31)


#==============================================================================
# hmd = '010620.KS'
# hhi = '009540.KS'
#==============================================================================


import sqlite3

con = sqlite3.connect("d:\\stock\\kospi.db")

cursor = con.cursor()
cursor.execute("select * from stock")


lKospi = cursor.fetchall()


HCAR = '005380.KS'
dfHCAR = web.DataReader(HCAR, 'yahoo', start, end)
dfHCAR = dfHCAR['Adj Close']
count = 1
lHighCorr = []
for item in lKospi:
    
#==============================================================================
#     if count > 1000:
#         break
#     print("{0:0>6}".format(item[1]) + ".KS")
#==============================================================================
    
    try:
        df = web.DataReader("{0:0>6}".format(item[1]) + ".KS",'yahoo', start, end)
        dfClose = df['Adj Close']
        dfConCat = pd.concat([dfHCAR,dfClose], axis = 1)
        dfConCat.columns = ['HCAR',item[2]]
#==============================================================================
#         print(type(dfConCat.corr()['HCAR'][1]))
#==============================================================================
        if dfConCat.corr()['HCAR'][1] > 0.8:        
            lHighCorr.append(item[2])
    except:
        print("hi")

    count += 1
    




print(lHighCorr)

#==============================================================================
#         dfConCat.columns = ['HCAR',item[2]]
#==============================================================================
        
 

    



#==============================================================================
# HCAR = '005380.KS'
# KCAR = '000270.KS'
# 
# LGE = '066570.KS'
# LGC = '051910.KS'
# 
# HCAR = LGE
# KCAR = LGC
# 
# 
# dfHMD = web.DataReader(HCAR, 'yahoo', start, end)
# dfHHI = web.DataReader(KCAR, 'yahoo', start, end)
# 
# 
# dfHMD_Adj = dfHMD['Adj Close']
# dfHHI_Adj = dfHHI['Adj Close']
# 
# 
# dfNormHMD = normalize(dfHMD_Adj)
# dfNormHHI = normalize(dfHHI_Adj)
# 
# 
# dfConCat = pd.concat([dfNormHMD, dfNormHHI], axis=1)
# 
# #==============================================================================
# # print(dfConCat)
# #==============================================================================
# 
# 
# dfConCat.columns = ['HCAR','KCAR']
# dfConCat.plot(figsize=(32,8))
# 
# print(dfConCat.corr())
#==============================================================================
#==============================================================================
# import KOSPI
# import datetime
# 
# start = datetime.datetime(2015,1,1)
# end = datetime.datetime(2016,1,1)
# 
# l = [HCAR, KCAR]
# 
# ldf = KOSPI.GetAdjustClose(l, start, end)
# 
#==============================================================================
