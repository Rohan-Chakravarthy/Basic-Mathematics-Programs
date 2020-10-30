from sympy import *
import numpy as np
def dal(U):
    x=Symbol('x')
    U=x*((U)-1)
    lim=limit(U,x,np.inf)   
    if (lim<1):
        print("The series diverges")
    elif (lim>1):
        print("The series converges")
    else:
        print("The test fails")
        

#define un+1/un
U=(2*x+1)*(2*x)/((2*x+2)*(2*x-1))
dal(U)
