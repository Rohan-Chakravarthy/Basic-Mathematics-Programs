def multmod(x,y,z):
    return (x*y)%z
def comm(set_, modulo):
    for i in range(len(set_)):
        for j in range(len(set_)):
            if multmod(set_[j], set_[i], modulo)!=multmod(set_[i], set_[j],modulo):
                print("The ring is not commutative")
                return None
    print("The ring is commutative")

def mul_iden(set_, modulo):
    for i in range(len(set_)):
        flag= True
        for j in range (len(set_)):
            if multmod(set_[j], set_[i], modulo)!=set_[j]:
                flag=False
                break
        if flag:
            iden= set_[i]
            print("Unity={}".format(iden))
            return iden
    print("The ring has no multiplicative identity")
    return None
comm([0,2,4],6)
mul_iden([0,2,4],6)
