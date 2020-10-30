# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:17:20 2020

@author: user
"""

from numpy import *
def pow(A,X,n):
    for i in range (1,n):
        y=A*X
        l=y[0]
        X=y/l
    print(X)
    print(l)
A=matrix([[25,1,2],[1,3,0],[2,0,-4]])
X=matrix([[1],[0],[0]])
pow(A,X,7)