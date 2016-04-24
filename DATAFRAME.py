# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:41:58 2016

@author: KBS
"""

import pandas as pd
import numpy as np

sr1 = pd.Series(np.random.randn(10)) * 100
sr2 = pd.Series(np.random.randn(10))

print(type(sr1.tolist()))

#==============================================================================
# l1 = sr1.tolist()
#==============================================================================

df1 = pd.DataFrame(sr1,columns=['test1'])
df2 = pd.DataFrame(sr2,columns=['test2'])

#==============================================================================
# df3 = df1.join(df2, how='outer')
#==============================================================================

print(df1.drop(1))

df3 = pd.concat([df1,df2],axis=1)

print(df3)


