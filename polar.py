# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:49:09 2020

@author: user
"""

import sympy
from sympy import sin,cos,simplify,diff,symbols
x, y, z, r, theta, phi, i, j, k, e_r, e_theta, e_phi =symbols("x, y, z, r, theta, phi, i, j, k, e_r, e_theta, e_phi ")
# x,y,z in spherical
m=r*sin(theta)*cos(phi)
n=r*sin(theta)*sin(phi)
t=r*cos(theta)
#the unit vectors of cartesian to spherical
p= (sin(theta)*cos(phi)*e_r)+(cos(theta)*cos(phi)*e_theta)-(sin(phi)*e_phi) 
q= (sin(theta)*sin(phi)*e_r)+(cos(theta)*sin(phi)*e_theta)+(cos(phi)*e_phi) 
s=(cos(theta)*e_r)-(sin(theta)*e_theta)
# function that has to be converted
f=(x*i+y*j+z*k)
w= simplify(f.subs([(x,m),(y,n),(z,t),(i,p),(j,q),(k,s)]))
print("The function in spherical co-ordinate is= ",w)
# since f is a vector: f1 is coeff of e_r, f2 is coeff of e_theta, f3 is coeff of e_phi f1=w.coeff(e_r)
f1=w.coeff(e_r)
f2=w.coeff(e_theta)
f3=w.coeff(e_phi)
#calculating divergence of f in spherical co-ordinates.
a=(1/r**2)*diff((r**2)*f1, r)
b=(1/(r*sin(theta)))*diff(f2*sin(theta),theta)
c=(1/(r*sin(theta)))*diff(f3,phi)
print("\n The divergence in spherical co-ordinates is =",a+b+c)
#calculating curl of f in spherical co-ordinates.
g1=diff(f3*sin(phi),theta)
g2=diff(f2,phi)
g3=(1/sin(theta))*diff(f1,phi)
g4=diff(r*f3,r)
g5=diff(r*f2, r)
g6=diff(f1,theta)
h1=(1/(r*sin(theta)))*(g1-g2)
h2=(1/r)*(g3-g4)
h3=(1/r)*(g5-g6)
print("Curl is (",h1,") e_r + (",h2,") e_theta + (",h3,") e_phi")