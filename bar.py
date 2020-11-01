import time as ti
import sys,getpass

def bar():
    t = 15
    m=1
    sys.stdout.write("[## %s" % (" " * t))
    sys.stdout.flush()
    sys.stdout.write("\b" * (t+1))
    for i in range(t):
        ti.sleep(1)
        sys.stdout.write("#")
        sys.stdout.flush()
    sys.stdout.write("]\nNow press enter to view score\n")

input("press entr to start")
print("\nplyr1\n")
bar()
a=getpass.getpass("")
print(len(a))
print("now plyr2\n")
ti.sleep(1)
bar()
b=getpass.getpass("")
print(len(b))
ti.sleep(0.5)
if len(a)>len(b):
    print("\nplyr1 win")
elif len(a)<len(b):
    print("\nplyr2 win")
else:
    print("\ntie")
