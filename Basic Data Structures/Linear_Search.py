# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:02:57 2020

@author: Monjur Bin Shams
"""

def linear_search(L,value):
    for i in range(len(L)):
        if(L[i]==value):
            return i
            
        else:
            i+=1
    return -1               
L = [10,12,13,14,15,16,17,24,28]
print("Please input your number:")
x = int(input())
num = linear_search(L, x)

if(num == -1):
    print("Number is not in the list")
else:
    print("number is at the index %s" %num)