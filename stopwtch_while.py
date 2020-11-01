import os, time

def c():
    os.system('clear')

h=s=m=0
e = input("press Enter to start\n")
c()
while (e != 'Enter'):
    print(""" %d hour: %d min : %d sec  

             press ctrl+z to stop """%(h,m,s))
    time.sleep(1)
    c()
    s+=1
    if(s == 60):
        s = 0
        m+=1
    if(m == 60):
        m = 0
        h+=1
