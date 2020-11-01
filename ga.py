import random

def a():
        r = ''
        for i in range(3):
            n = random.randint(1,999)
            r += chr(n)
        print(r)
        b=input("\nnow u type: ")
        if r==b:
            print("good\n")

a()
