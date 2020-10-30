def f(x):
    return 1/(1+x**2)
def simp(a,b,n):
    h=(b-a)/n
    r=f(a)+f(b)
    for i in range (1,n):
        if(i%3==0):
            r=r+2*f(a+i*h)
        else:
            r=r+3*f(a+i*h)
    return ((3*h)/8)*r
print(simp(0,1 ,4 ))
    
            
        