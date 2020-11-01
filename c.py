"""
x = input('''available operators -,+,×,÷
calculate  : ''')


if '+' in x:
   a = x.split('+')
   pl = int(a[0])+int(a[1])
   print(pl)

if '×' in x:
   b = x.split('×')
   mul = int(b[0])+int(b[1])
   print(mul)

if '÷' in x:
   c = x.split('÷')
   div = int(c[0])+int(c[1])
   print(div)

if '-' in x:
   d = x.split('-')
   sub = int(d[0])+int([1])
   print(sub)
"""
"""
print('\033c')

while True:

 x = input('''available operators -,+,×,÷
 calculate  : ''')


 if '+' in x:
   a = x.split('+')
   pl = int(a[0])+int(a[1])
   print('= ',pl)

 if '×' in x:
   b = x.split('×')
   mul = int(b[0])*int(b[1])
   print('= ',mul)

 if '÷' in x:
   c = x.split('÷')
   div = int(c[0])/int(c[1])
   print('= ',div)

 if '-' in x:
   d = x.split('-')
   sub = int(d[0])-int(d[1])
   print('= ',sub)
"""
"""
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
"""
"""
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
"""
"""
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
"""
"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
"""
"""
def rec(x):
  if(x > 0):
    r= x + rec(x - 1)
    print(r)
  else:
    r= 0
  return r

print("rec results")
rec(6)
"""
def rec(x):
  if(x>0):
    r= x+rec(x-1)
    print(r)
  else:
    r=0
  return r
print("rec results")
rec(10)
