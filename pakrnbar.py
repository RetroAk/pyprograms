import time,os,sys
from threading import Thread
import getpass

def first():
 print("time is running !\n")
 i = 0
 while (i < 30):
  time.sleep(0.15)
  print("=",end='',flush=True)
  i += 1

def second():
 x = getpass.getpass("")
 print("\nyour score is ;\n")
 print(len(x))
 print()

def third():
   time.sleep(5)
   print("\n\ntimout! press enter to see your score")

t1 = Thread(target = first)
t2 = Thread(target = second)
t3 = Thread(target = third)

os.system("clear")

input("press enter to start Game ")

os.system("clear")

t1.start()
t2.start()
t3.start()
