from scipy.integrate import *
import sympy as sp
import numpy as np
x=sp.Symbol('x')
def f(x):
    return sp.exp(x)
def gamma(p,a,b):
    q=quad(f,a,b)
    print(q)

gamma(2,0,10)