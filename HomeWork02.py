# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:27:48 2024

@author: GENE
"""

a = 0
b = 0
c = 0

a = int(input("Input A："))
b = int(input("Input B："))
c = int(input("Input C："))

if a > b+c or b > a+c or c > a+b:
    print("Is a Triangle!")
else:
    print("Not a Triangle!")

if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
    print("Is a Right Triangle!")
else:
    print("Is a Right Triangle!")
