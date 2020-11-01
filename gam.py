import random,string

def a():
    a=string.digits
    b=print(''.join(random.choice(a)  for i in range(3)))
    c=input("type: ")
    if (b == c):
        print("\ngood\n")

def b():
    a=string.digits
    print(''.join(random.choice(a)  for i in range(4)))

def c():
    a=string.digits
    print(''.join(random.choice(a)  for i in range(5)))

def d():
    a=string.digits
    print(''.join(random.choice(a)  for i in range(6)))

def e():
    a=string.digits
    print(''.join(random.choice(a)  for i in range(7)))

def f():
    a=string.digits
    print(''.join(random.choice(a)  for i in range(8)))

def g():
    a=string.digits
    print(''.join(random.choice(a)  for i in range(9)))

def h():
    a=string.digits
    print(''.join(random.choice(a)  for i in range(10)))

def i():
    a=string.digits
    print(''.join(random.choice(a)  for i in range(11)))

input("enter to start")
a()
b()
c()
d()
e()
f()
g()
h()
i()

