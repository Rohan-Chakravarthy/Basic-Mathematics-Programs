z_n = {0,1,2,3,4,5,6,7,8,9}
n = 10
subset = {0,2,4,6,8}
add = lambda x, y: (x+y) % n 
mult = lambda x, y: (x*y) % n
ideal_add, ideal_mult, subring = True, True, True
for i in subset:
    for j in subset:
        if add(i, -j) not in subset or mult(i,j) not in subset:
            subring = False
            ideal_add = False
    if ideal_add:
        for r in z_n:
            if mult(r, i) not in subset:
                ideal_mult = False
if subring: 
    print("18PEM22007 \n The given subset", subset," is a subring of", z_n)
else:
    print("(18PEM22007) \n The given subset", subset," is not a subring of", z_n)
if ideal_add and ideal_mult:
    print("18PEM22007 \n The given subset", subset," is an ideal of", z_n)
else :
    print("18PEM22007 \n The given subset", subset," is not an ideal of", z_n)
        