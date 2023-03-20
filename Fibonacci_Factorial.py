# -*- coding: utf-8 -*-
"""
Fibonacci and Factorial
Created on Mon Mar 20 10:34:48 2023


@author: Shahriar
"""
from time import time,sleep

#%% Fibonacci  ----------------------------------------------------------

def fibo_rec(n): # recusrsion
    if n<2:
        return 1
    return fibo_rec(n-1)+fibo_rec(n-2)


#----------------------------------------------------------
def fibo_memo(n,mem={}): # memoization
    if n<2:
        return 1
    else:
        if n in mem:
            return mem[n]
        else:
            mem[n]= fibo_memo(n-1,mem)+fibo_memo(n-2,mem)
    return mem[n]


#%% Factorial  ----------------------------------------------------------
def fac_rec(n):
    if n<2:
        return 1
    return n*fac_rec(n-1)
#----------------------------------------------------------
def fac_memo(n,mem={}):
    if n<2:
        return 1
    else:
        if n in mem:
            return mem[n]
        else:
            mem[n]= n*fac_memo(n-1,mem)
        
    return mem[n]






if __name__=='__main__':
    # Test Values
    #%% Fibonacco
    res_1=fibo_rec(10)
    res_2=fibo_rec(5)
    
    res_3=fibo_memo(10)
    res_4=fibo_memo(5)
    
    
    # Get time
    t1=time()
    res_rec=fibo_rec(30)
    t2=time()
    res_mem=fibo_memo(200)
    t3=time()
    
    time_rec=t2-t1
    time_mem=t3-t2
    
    
    
    
    #%% Factorial
    t1=time()
    res_rec_fac=fac_rec(2000)
    t2=time()
    res_mem_fac=fac_memo(2000)
    t3=time()
    
    time_rec_fac=t2-t1
    time_mem_fac=t3-t2
    
    
