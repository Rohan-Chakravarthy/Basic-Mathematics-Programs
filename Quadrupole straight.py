# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:31:00 2019

@author: user
"""

from numpy import cos,hypot,arctan,linspace,meshgrid,array,arange
import matplotlib.pyplot as plt
q=1.602e-19
k=9.0e9
s=1e-12
x=linspace(-1e-11,1e-11,100)
y=x.copy()
x, y=meshgrid(x, y)
t=arctan(y/x)
r=hypot(x, y)
a=(15/2)*((s/r)**4)
b=(2*(s**2)/(r**2))*((6*((cos(t))**2))-1)
V=((k*q)/r)*(a+b)
fig=plt.figure()
ax=fig.add_subplot(111)
levels=array([10**pw for pw in linspace(0,5,20)])
levels=sorted(list(-levels) + list(levels))
ax.contour(x,y,V,levels=levels,colors='k',linewiths=0.5)
plt.show()