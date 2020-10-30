#18pem22007
from sympy import *
x, y , z, i, c, r, t = symbols("x, y, z, i, c, r, t")
def milthom(u, v):
    if v==0:
        f1 = diff(u, x)
        f2 = diff(u, y)
        a = integrate(f1.subs([(x, z) , (y, 0)]), z)
        b = integrate(f2.subs([(x, z) , (y, 0)]), z)
        w = a - i * b + c
        print("f(z) = ", w)
    if u==0:
        f1 = diff(v, x)
        f2 = diff(v, y)
        a = integrate(f1.subs([(x, z) , (y, 0)]), z)
        b = integrate(f2.subs([(x, z) , (y, 0)]), z)
        w = b + i * a + c
        print("f(z) = ", w)
        
        

def milpol(u, v):
    if v==0:
        f1 = diff(u, r)
        f2 = diff(u, t)
        w = integrate(f1.subs([(r, z), (t, 0)]), z) - i * integrate((f2*(1/r)).subs([(r, z), (t, 0)]), z) + c
        print("f(z) =", w)
    if u==0:
        f1 = diff(v, r)
        f2 = diff(v, t)
        w = integrate(((1/r)*f2).subs([(r, z), (t, 0)]), z) - i * integrate(f1.subs([(r, z), (t, 0)]), z) + c
        print("f(z) =", w)
        
milthom(2 * x - x**3 + 3 * x * y**2 , 0)
milthom(0, 3 * x**2 * y - y**3)
milpol((r + (1/r)) * cos(t) , 0)
milpol(0 , t)