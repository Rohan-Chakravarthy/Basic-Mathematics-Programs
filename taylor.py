#Taylor series


import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol,sin,diff
from math import factorial
x=Symbol('x')
f=sin(x)
def taylor(f,a,n):
    p=0
    for i in range (0,n):
        p=p+(((diff(f,x,i)).subs(x,a))*((x-a)**i))/factorial(i)
        i=i+1
    return p
x1=np.linspace(-5,5,100)
y1=[]
for j in range (1,10,2):
    fun=taylor(f,0,j)
    print('The taylor series approximation at n='+str(j),'is',fun)
    for k in x1:
        y1.append(fun.subs(x,k))
    plt.plot(x1,y1,label='order'+str(j))
    y1=[]
plt.plot(x1,np.sin(x1),color='black',label='sin of x')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('taylor series approximation')
plt.show()


            
    