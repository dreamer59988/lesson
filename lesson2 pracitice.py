# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:05:37 2022

@author: user
"""

#y=0
#for i in range(1,6):
  #  x= input(f'enter {i} number:')
  #  y=y+int(x)
#print (f'the result={y}')

a="*"
b=" "
c=1
d=6
e=4
i=1
tmax=0
tmin=0
print(f"1 {b} 1")
#print("\n")
print("\n")
print("aaaaa")

for y in range(c,e):
    if i == 1:
        tmax=d/2
        tmin=d/2
        print("next")
    else:
        tmax=d/2+1
        tmin=d/2-1
        for i in range(c,d):
           if i <= tmax and i>= tmin:
              print(a,end="")
             
           else:
              print(b,end="")
    