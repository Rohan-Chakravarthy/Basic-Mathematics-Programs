# Differential equations

from sympy import Symbol,Derivative,Eq,Function,pprint,dsolve,exp
x=Symbol('x')
y=Function('y')
y1=Derivative(y(x),x)
y2=Derivative(y1,x)
z=Eq(y2-6*y1+10,exp(x))
z1=dsolve(z)
pprint(z1)