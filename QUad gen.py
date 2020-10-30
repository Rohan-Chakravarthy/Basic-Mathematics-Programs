import matplotlib.pyplot as pl
import numpy as np
#defining potential
def pot(r,d,u):
    V=(9.0e9*q)/(r**2+d**2+2*d*r*np.cos(u-t))
    return V
#plotting
q=1.6e-19
t=np.linspace(-360,360,1000)
p=pot(1.0e-19,1.0e-19,0)+pot(1.0e-19,3.0e-19,0)+pot(1.0e-19,-1.0e-19,np.pi)+pot(1.0e-19,-3.0e-19,n


    