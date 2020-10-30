from numpy import cos,hypot,arctan,linspace,meshgrid,array,arange
import matplotlib.pyplot as plt
q=1.602e-19
k=9.0e9
s=1e-12
x=linspace(-1e-12,1e-12,100)
y=x.copy()
x, y=meshgrid(x, y)
t=arctan(y/x)
r=hypot(x, y)
a=(3/4)*((s**2)/r)*cos(2*t)
b=s*cos(t)
V=-((k*q)/(r**2))*(a+b)
fig=plt.figure()
ax=fig.add_subplot(111)
levels=array([10**pw for pw in linspace(0,5,20)])
levels=sorted(list(-levels) + list(levels))
ax.contour(x,y,V,levels=levels,colors='k',linewiths=0.5)
plt.show()