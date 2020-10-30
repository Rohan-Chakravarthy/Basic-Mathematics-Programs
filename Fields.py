def multmod(x,y,z):
    return (x*y)%z
def mul_iden(set_, modulo):
    for i in range(len(set_)):
        flag= True
        for j in range (len(set_)):
            if multmod(set_[j], set_[i], modulo) != set_[j]:
                flag=False
                break
        if flag:
            iden = set_[i]
            print("Unity = {}".format(iden))
            return iden
    print("No multiplicative identity")
    
def mult_invertible(set_, modulo):
    e = mul_iden(set_, modulo)
    if e is not None:
        for i in range(1,len(set_)):
            flag = False
            for j in range(1,len(set_)):
                if multmod(set_[j],set_[i],modulo) == e:
                    flag = True
                    break
            if flag == False:
                print("Not every non-zero element has a multiplicative inverse")
                return
    if flag:
        print("Every element has a multiplicative inverse")
        
mult_invertible([0,2,4,6,8],10)


