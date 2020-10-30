def lagi(X,Y,a):
    res=0 
    b=len(X) 
    for i in range (0,b):
        c=1
        for j in range (0,b):
            if (i!=j):
                c=c*((a-X[j-1])/(X[i-1]-X[j-1]))
        res = res + c*Y[i-1]
    print(res)

X=[0,1,3,4]
Y=[-12,0,6,12]
lagi(X,Y,2)
