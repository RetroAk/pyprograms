import os
from random import randint as r

def c():
    os.system('clear')
c()

def ab():
    c()
    a=['rock','paper','scissors']
    pc=a[r(0,2)]
    user=False
    while user==False:
        user=input("rock,paper,scissors?")
        if user==pc:
            print("adthe match id..ith tie aayi poi ;(")
            exit()
        elif user=="rock":
            if pc=="paper":
                print("You lose!",pc,"ninte",user,"pothinj!")
                exit()
            else:
                print("You win!",user,pc, "pothinj")
        elif user=="paper":
            if pc=="scissors":
                print("You lose!",pc,"ninte",user,"murich")
                exit()
            else:
                print("You win!",user,pc,"moodi")
        elif user=="scissors":
            if pc=="rock":
                print("You lose...",pc,user,"potich")
                exit()
            else:
                print("You win!",user,pc,"murich")
        else:
            print("pottaah!..spelling correct aak")
        user=False
        pc=a[r(0,2)]
i = input("press entr to start or n to exit")
if i=="":
    ab()
elif i=='n':
    print("exit")
    exit()
