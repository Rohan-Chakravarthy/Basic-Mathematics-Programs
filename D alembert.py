from sympy import *
import numpy as np
x=Symbol('x')
def dal(Un1,Un):
    U=Un1/Un
    lim=limit(U,x,np.inf)   
    if (lim<1):
        print("The series converges ")
    elif (lim>1):
        print("The series diverges")
    else:
        print("The D'Alembert test fails")
        print("Now by raabes test")
        U2=x*((U)-1)
        lim=limit(U2,x,np.inf)   
        if (lim<1):
            print("The series diverges")
        elif (lim>1):
            print("The series converges")
        else:
            print("The Raabe test fails")
        
Un=(2*x+2)*(2*x-1)
Un1=(2*x+1)*(2*x)
dal(Un1,Un)