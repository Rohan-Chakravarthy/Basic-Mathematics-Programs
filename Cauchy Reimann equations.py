from sympy import *
x, y ,r ,t= symbols("x, y, r, t")
#u = (log(x**2 + y**2))/2
#v = atan(y/x)
#ux = simplify(diff(u, x))
#uy = simplify(diff(u, y))
#vx = simplify(diff(v, x))
#vy = simplify(diff(v, y))
#if ux == vy and uy == -vx :
    #print("Function satisfies CR equations")
#else:
    #print("Function does not satisfy CR equations")
    
    
    
u = (r + (1/r)) * cos(t)
v = (r - (1/r)) * sin(t)
ur = simplify(diff(u, r))
ut = simplify(diff(u, t))
vr = simplify(diff(v, r))
vt = simplify(diff(v, t))
if ur == simplify((1/r)*vt) and ut == simplify(-r*vr) :
    print("Function satisfies CR equations")
else:
    print("Function does not satisfy CR equations")
    
print("18PEM22007")