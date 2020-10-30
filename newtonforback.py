from sympy import *
def nbf(F,X,b):
    a=len(X)
    Y1 =[]; Y2=[]; Y3=[]; Y4=[]; Y5=[] ; Y6=[]
    a1=len(F)
    for i in range (1,a1):
        x=F[i]-F[i-1]
        Y1.append(x)
    a2=len(Y1)
    for i in range (1,a2):
        x=Y1[i]-Y1[i-1]
        Y2.append(x)
    a3=len(Y2)
    for i in range (1,a3):
        x=Y2[i]-Y2[i-1]
        Y3.append(x)
    a4=len(Y3)
    for i in range (1,a4):
        x=Y3[i]-Y3[i-1]
        Y4.append(x)
    a5=len(Y4)
    for i in range (1,a5):
        x=Y4[i]-Y4[i-1]
        Y5.append(x)
    a6=len(Y5)
    for i in range (1,a6):
        x=Y5[i]-Y5[i-1]
        Y6.append(x)
    a7=len(Y6)
    
        
    h=X[1]-X[0]
    #p=(b-X[a-1])/h
    p=(b-X[0])/h
    #res=F[a1-1]+p*Y1[a2-1]+(p*(p+1)*Y2[a3-1])/factorial(2)+(p*(p+1)*(p+2)*Y3[a4-1])/factorial(3)
    #res=F[0]+p*Y1[0]+(p*(p-1)*Y2[0])/factorial(2)+(p*(p-1)*(p-2)*Y3[0])/factorial(3)
    res=F[0]+p*Y1[0]+(p*(p-1)*Y2[0])/factorial(2)+(p*(p-1)*(p-2)*Y3[0])/factorial(3)+(p*(p-1)*(p-2)*(p-3)*Y4[0])/factorial(4)+(p*(p-1)*(p-2)*(p-3)*(p-4)*Y5[0])/factorial(5)+(p*(p-1)*(p-2)*(p-3)*(p-4)*(p-5)*Y6[0])/factorial(6)
    #res=F[a1-1]+p*Y1[a2-1]+(p*(p+1)*Y2[a3-1])/factorial(2)+(p*(p+1)*(p+2)*Y3[a4-1])/factorial(3)+(p*(p+1)*(p+2)*(p+3)*Y4[a5-1])/factorial(4)+(p*(p+1)*(p+2)*(p+3)*(p+4)*Y5[a6-1])/factorial(5)+(p*(p+1)*(p+2)*(p+3)*(p+4)*(p+5)*Y6[a7-1])/factorial(6)
    print(res)

#F=[0.7071,0.766,0.8192,0.866]
#X=[45,50,55,60] 
F=[10.63,13.03,15.04,16.81,18.42,19.9,21.27]
X=[100,150,200,250,300,350,400] 
nbf(F,X,125)