def c_hcf(x,y):
    if x<y:
        sm=x
    else:
        sm=y
    for i in range(1,sm+1):
        if ((x%i==0) and (y%i==0)):
            hcf=i
    return hcf

n1=int(input("entr 1: "))
n2=int(input("entr 2: "))
print("the hcf of {0},{1} is {2}".format(n1,n2,c_hcf(n1,n2)))
