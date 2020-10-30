from sympy import *
from sympy.series.sequences import SeqFormula
n = Symbol('n', integer = True)
x = Symbol('x')
func = x*(pi - xqq)
limits = (x,0,pi)
def a_0(func, limits):
    x, L = limits[0], limits[2] - limits[1]
    a0 = Integral((2/L) * func, limits).doit()
    return SeqFormula(a0/2) 
def a_n(func,limits):
    x, L = limits[0], limits[2] - limits[1]
    cos_term = cos(n*pi*x/L)
    an = Integral((2/L) * func * cos_term, limits).doit()
    return SeqFormula(an * cos_term, (n, 1, oo))
s1 = a_0(func, limits)
s2 = a_n(func, limits)
string=''
for m in range(8) :
    if s2[m]==0:
        pass
    else:
        string+=str(s2[m])

def fourier_sin_seq(func, limits):
    x, L = limits[0], limits[2] - limits[1]
    sin_term = sin(n * pi * x / L)
    bn= Integral((2/L) * func * sin_term,limits).doit()
    return SeqFormula(bn * sin_term, (n, 1, oo))
s3 = fourier_sin_seq(func, limits)
string1=''
for p in range(4):
    if s3[p]==0:
        pass
    else:
        string1+="("+str(s3[p])+")" + "+"
        
print("\n\nFourier Cosine Series:\n")
print("f(x) = "+str(s1[0])+string+"+"+"....")
print("\n\nFourier Sine Series :\n")
print("f(x) = "+string1+"....")