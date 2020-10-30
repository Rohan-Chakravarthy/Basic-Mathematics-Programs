# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:06:31 2020

@author: rohan
"""
#18pem22007
from sympy import *
x, y = symbols("x, y")
def orth(u, v):
    print("u =", u, "\n v =", v)
    ux = diff(u, x)
    uy = diff(u, y)
    vx = diff(v, x)
    vy = diff(v, y)
    a, b = -ux/uy , -vx/vy
    m = simplify(a * b)
    if m == -1:
        print("u and v are orthogonal trajectories \n\n")
    else:
        print("u and v are not orthogonal trajectories")

orth(x**3 - 3 * y**2 * x , 3 * x**2 * y - y**3)
orth(exp(-x) * x * sin(y) - exp(-x) * y * cos(y) , exp(-x) * x * cos(y) + exp(-x) * y * sin(y))