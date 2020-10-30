from sympy import *
import math as np
n=Symbol('n')
a=n**2
lim=limit(a,n,np.inf)
l=(np.isinf(float(lim)))
if(l==True):
    print("divergent")
elif(l==False):
    print("convergent")
