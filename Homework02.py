# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:10:32 2024

@author: USER
"""

for a in range(1,10):
    for b in range(9,1,-1):
        print(b,"*",a,"=",a*b,sep="",end="\t")
    print()