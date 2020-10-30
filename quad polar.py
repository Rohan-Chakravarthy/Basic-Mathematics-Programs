import matplotlib.pyplot as plt
import numpy as np
k=9.0e9
q=1.9e-19
d=1.0e1
t=np.linspace(0,2*np.pi,10000)
i=1
for i in range (7,15):
    V=(3*k*q*(d**2)/(2*(i**3)))*np.cos(2*t)
    plt.polar(t,V,color='black')
    i=i+5
for i in range (-15,-7):
    V=(3*k*q*(d**2)/(2*(i**3)))*np.cos(2*t)
    plt.polar(t,V,color='black')
    i=i+5
plt.show()