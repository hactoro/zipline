# -*- coding: utf-8 -*-
"""
Created on Mon May  2 00:03:37 2016

@author: KBS
"""

import numpy


a = numpy.arange(4)
b = a.reshape(2,2)

print(b)

c = numpy.dot(b,b)
print(c)