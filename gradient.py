# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:02:03 2020

@author: rohan
"""

from sympy import *
x, y, z = symbols("x, y, z")
def grad(f):
    a = diff(f, x)
    b = diff(f, y)
    c = diff(f, z)
    print("Gradient is (", a,")i + (", b,")j + (", c,")k")

f1 = 2*x**2*y**3*z
grad(f1)

f2 = 3*x**2 + 2*y**3 - 5*z      
grad(f2)