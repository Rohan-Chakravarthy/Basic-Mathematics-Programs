# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:20:07 2020

@author: rohan
"""
#18pem22007
from sympy import *
x, y, r, t = symbols("x, y, r, t")
def harcart(u, v):
    uxx , uyy = diff(u, x, x) , diff(u, y, y)
    vxx , vyy = diff(v, x, x) , diff(v, y, y)
    a, b = simplify(uxx + uyy) , simplify(vxx + vyy)
    print("The laplacian of u is", a,"and v is",b)
    if a == 0 and b == 0:
        print("The functions are harmonic")
    else:
        print("The functions are not harmonic")
        
def harpol(u, v):
    ur, urr, utt = diff(u, r), diff(u, r, r) , diff(u, t, t)
    vr, vrr, vtt = diff(v, r), diff(v, r, r) , diff(v, t, t)
    a = simplify(urr + (1/r) * ur + (1 / r**2) * utt)
    b = simplify(vrr + (1/r) * vr + (1 / r**2) * vtt)
    print("The laplacian of u is", a,"and v is",b)
    if a == 0 and b == 0:
        print("The functions are harmonic")
    else:
        print("The functions are not harmonic")
        
harcart(x**3 - 3 * x * y**2 , 3 * x**2 * y - y**3)
harcart(cos(x) * sinh(y) , sin(x) * cosh(y))
harpol((1 / r**2) * cos(2 * t) , -(1 / r**2) * sin(2 * t))
harpol(r**2 * cos(2 * t) , r**2 * sin(2 * t))