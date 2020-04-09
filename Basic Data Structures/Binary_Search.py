# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:56:43 2020

@author: Monjur Bin Shams
"""
import os
os.system("cls")
#Lets take a sorted list

L = [1,4,5,6,9,11,22,25,25,28]

x = int(input())

lower = 0
upper = len(L)-1

while (upper):
    if (x>L[upper]):
        print("number is not in the list")
        break
    else:
        mid = (lower + upper)//2
        
        if(L[mid]<x):
            lower = mid + 1
        elif(L[mid]>x):
            upper = mid - 1
            
        elif(L[mid]==x):
            print("number is found")
            break