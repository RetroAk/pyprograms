import random,os
a = "stone"
b = "paper"
c = "scissor"
x = [a,b,c]
y = random.choice(x)
os.system('clear')
def bot():
 print("\ncomputer : "+y)
def same():
 print("\nTIE ! try again ")
def won():
 print("\nYou WON !")
def lose():
 print("\nYou LOSE !")
def main():
    st = input("\nchoose your's [1] stone | [2] paper | [3] scissor | [0] exit : ")
    if (st == '1') and (y == a):
     bot()
     same()
    if (st == '2') and (y == b):
     bot()
     same()
    if (st == '3') and (y == c):
     bot()
     same()
    if (st == '1') and (y == b):
     bot()
     lose()
    if (st == '1') and (y == c):
     bot()
     won()
    if (st == '2') and (y == a):
     bot()
     won()
    if (st == '2') and (y == c):
     bot()
     lose()
    if (st == '3') and (y == a):
     bot()
     lose()
    if (st == '3') and (y == b):
     bot()
     won()
    if (st == '0'):
     print("\nexited")
     exit()
while(True):
 main()
