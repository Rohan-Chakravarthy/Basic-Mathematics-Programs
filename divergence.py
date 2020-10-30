# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:58:56 2020

@author: rohan
"""
Abs
from sympy import *
x, y, z = symbols("x, y, z")
def div(a, b, c):
    print("Divergence is",diff(a, x) + diff(b, y) + diff(c, z))

div(2*x**2*y, 3*x, 4*z*x)
div(x*y*z, 3*y*x**2, x*z**2 - z*y**2)