#Limit of a function


from sympy import Symbol,limit,sin,pprint
x=Symbol('x')
y=sin(x)/x
pprint(y)
z=limit(y,x,0)
print(z)
