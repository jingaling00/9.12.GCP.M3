# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:05:05 2022

@author: jingy
"""

def multiples(x,y,n):
    """
    Python program to add multiples of
    x and y that are strictly less than n.
    """
    x_mults = []
    y_mults = []
    for i in range(x,n,x):
        x_mults.append(i)
    for j in range(y,n,y):
        y_mults.append(j)
    total_sum = sum(x_mults) + sum(y_mults)
    return total_sum

def fibo(n):
    fibos = [0,1]
    for i in range(2,n+1):
        nextt = (fibos[i-1])+(fibos[i-2])
        fibos.append(nextt)
    fibos.remove(0)
    return fibos

def fiboEven(n):
    fibos = [0,1]
    for i in range(2,(3*n)+1):
        nextt = (fibos[i-1])+(fibos[i-2])
        fibos.append(nextt)
    fibos.remove(0)
    
    evens = []
    for ele in fibos:
        if ele%2 == 0:
            evens.append(ele)
    return evens

if __name__ == '__main__':
    print(multiples(3,5,10)) # returns 23
    print(fibo(4)) # returns [1,1,2,3]
    print(fiboEven(10)) # returns [2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040]
    
    
        
        