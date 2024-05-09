# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

odd = 0
s = 0

print()
print("同時被5及15整除之數：",end="")

for i in range(1,101):
    if i % 2 == 1:
        odd += i
#        print(i,end=" ")
    if i % 7 == 0:
        s += i
#        print(i,end=" ")
    if i % 15 == 0:
        print(i,end=" ")
        
print()
print("奇數和：",odd)
print("7整除之和：",s)
