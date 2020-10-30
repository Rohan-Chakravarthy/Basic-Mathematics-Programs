# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:05:21 2020

@author: rohan
"""

from sympy import *
x, y, z = symbols("x, y, z")
def curl(a, b, c):
    l = diff(c, y) - diff(b, z)
    m = diff(c, x) - diff(a, z)
    n = diff(b, x) - diff(a, y)
    print("Curl is (", l,")i - (", m,")j + (", n,")k")

curl(y**2 + z**3 , 2*x*y - 5*z , 3*x*z**2 - 5*y)
curl(3*y*z , 2*x**2 , 5*x*y)