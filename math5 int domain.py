def multmod(x,y,z):
    return (x*y)%z
def mul_iden(set_, modulo):
    for i in range(1,len(set_)):
        flag= True
        for j in range (1,len(set_)):
            if multmod(set_[j], set_[i], modulo) == 0:
                flag=False
                break
        if flag == False:
            print("Zero divisors exist so the given ring is not an integral domain")
            return 
    if flag:
        print("No zero divisors exist so the given ring is an Integral Domain")


mul_iden([0,2,4,6,8],10)