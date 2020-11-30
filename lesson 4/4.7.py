from itertools import count
from math import factorial as fac

def fibo_gen():
     for el in count(1):
         yield fac(el)

gen = fibo_gen()
x = 0
for i in gen:
     if x < 15:
         print(i)
         x += 1
     else:
         break