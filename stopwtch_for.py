import time, os
def c():
    os.system('clear')
h=0
input("press enter to start")
for m in range(0, 60):
    for s in range(0, 60):
        time.sleep(1)
        c()
        print(h,"hour:", m,"min:", s,"""sec\n
                press ctrl+z to stop""")
        s+=1
    
