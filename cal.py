import os
os.system('clear')
def p():
    print("\n >>>",b)

print("            CALCULATOR             ")
a=input('''      Choose:
             1- AdD
             2- SubstracT
             3- MultiplY
             4- DividE
             5- MoD\n
             :> ''')

if a=='1':
    r=int(input("\n entr 1st num: "))
    s=int(input(" entr 2nd num: "))
    b=r+s
    p()
elif a=='2':
    r=int(input("\n entr 1st num: "))
    s=int(input(" entr 2nd num: "))
    b=r-s
    p()
elif a=='3':
    r=int(input("\n entr 1st num: "))
    s=int(input(" entr 2nd num: "))
    b=r*s
    p()
elif a=='4':
    r=int(input("\n entr 1st num: "))
    s=int(input(" entr 2nd num: "))
    b=r/s
    p()
elif a=='5':
    r=int(input("\n entr 1st num: "))
    s=int(input(" entr 2nd num: "))
    b=r%s
    p()
else:
    print("\n entr crct choice ;)\n")
    exit()
