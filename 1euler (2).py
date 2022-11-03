# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:49:56 2022

@author: Maria
"""

def mensheYKratnyj(menshe, kratnyj1, kratnyj2):
    sum=0
    for x in range(menshe):
        if (x%kratnyj1==0 or x%kratnyj2==0):
            #print(x)
            sum+=x
    return sum        
            
print(mensheYKratnyj(10, 3, 5))
print(mensheYKratnyj(1000, 3, 5))