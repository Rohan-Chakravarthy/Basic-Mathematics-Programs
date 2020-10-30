# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:16:18 2020

@author: rohan
"""

from sympy import *
x, y, z, rho, phi, e_rho, e_phi, e_z = symbols("x, y, z, rho, phi, e_rho, e_phi, e_z")
m = rho*cos(phi)
n = rho*sin(phi)
f = 3*y + x**2 + z**2
w = f.subs([(x,m) , (y,n) , (z,z)])
print("The function in cylindrical coordinates is", w)
a = diff(w, rho)
b = (1/rho)*diff(w, phi)
c = diff(w, z)
print("Gradient is (",a ,") e_rho + (", b,") e_phi + (", c,") e_z")

p = (1/rho)*diff(rho*a , rho)
q = (1/(rho**2))*diff(w , phi ,2)
r = diff(w ,z ,2)
print("The laplacian is", simplify(p + q + r))