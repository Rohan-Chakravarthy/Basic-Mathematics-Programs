import numpy as np
import matplotlib.pyplot as pl
fig=pl.figure()
x=np.arange(-20,20,0.001)
n=100
a=1
y=0
for i in range (1,n,2):
   y+=((2*a)/(i*np.pi))*np.sin(i*x)



pl.plot(x,y)
pl.axhline(y=0)
pl.axvline(x=0)
pl.show()