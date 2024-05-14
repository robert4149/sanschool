# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:53:19 2024

@author: GENE
"""

import random
a = random.randrange(5,101,5)
b = random.randrange(5,101,5)
c = random.randrange(5,101,5)
d = random.randrange(5,101,5)
e = random.randrange(5,101,5)

print(a,b,c,d,e)

print(a,end=" ")

while b == a:
    b = random.randrange(5,101,5)
print(b,end=" ")
    
while c == b or c == a:
    c = random.randrange(5,101,5)
print(c,end=" ")

while d == c or d == b or d == a:
    d = random.randrange(5,101,5)
print(d,end=" ")

while e == d or e == c or e == b or e == a:
    e = random.randrange(5,101,5)
print(e,end=" ")
        