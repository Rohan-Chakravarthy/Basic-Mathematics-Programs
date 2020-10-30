# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:59:44 2020

@author: rohan
"""

from sympy import *
z, i = symbols("z, i")
def cauchy(function, curve, discontinuity, n):
    a = simplify(curve.subs([(z, discontinuity)]))
    if a < 0:
        b = (diff(function, z, n - 1)).subs([(z, discontinuity)])
        c = (2 * pi * i * b) / (factorial(n - 1))
        print("The integral is equal to", c)
    else:
        print("The integral is equal to 0")
        
        
cauchy(z**2 - z + 1 , abs(z) - 2, 1, 1)
cauchy(z**2 - z + 1 , abs(z) - 0.5, 1, 1)
cauchy(z**2 - z + 1 , abs(z - 2) - 1.5, 1, 1)
cauchy(sin(pi * z) , abs(z + 2) - 1, pi, 1)
cauchy(z**3 + 1 , abs(z - 2) - 3, 4, 2)
        
        
    
    
