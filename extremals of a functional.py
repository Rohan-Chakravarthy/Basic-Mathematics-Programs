#Name: Rohan       Roll Number: 18PEM22007
from sympy import *
f = Function('f')
x = Symbol('x')
y = Symbol('y')
k=Symbol('k')
y = f(x)
y1 = f(x).diff(x)
def F(x, y, y1):
    return (y * (1 + y1**2))**(1/2)
Eul = F(x, y, y1) - y1 * diff(F(x, y, y1), y1) - k
sol = dsolve(Eul, f(x))
print("The extremal of the given functional is y = ", sol.rhs)

