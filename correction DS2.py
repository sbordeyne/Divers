# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 13:37:42 2015

@author: Simon
"""
import matplotlib.pyplot as plt
import numpy as np

def PGCD(a,b):
    r=a%b
    if r==0:
        return b
    else:
        r=a%b
        a=b
        b=r
        return PGCD(a,b)
    pass

"""def a(x,L):
    if 0<=x<=L:
        return x
    elif L<=x<=4*L:
        return (4*L-x)/3
    else:
        return 0
    pass
def impaire(x,L):
    if x>=0:
        return a(x,L)
    elif x<=0:
        return -a(-x,L)
    pass
def y(x,L):
    if -4*L<=x<=4*L:
        return impaire(x,L)
    else:
        y(x-4*L,L)
    pass"""
    
def y(x):
    L=1.
    T=8*L
    if x>=0 and x<=L:
        return x
    elif x>=L and x<=4*L:
        return (4*L-x)/3.
    elif x>=-4*L and x<=0:
        return -y(-x)
    elif x>0:
        return y(x-(x//T)*T)
    else:
        return y(x+((np.abs(x)//T)+1)*T)
    pass
x=np.arange(-15,15.01,0.01)
f=np.vectorize(y)
plt.plot(x,f(x))
plt.xlabel("distances(m)")
plt.ylabel("oscillations")
plt.title("Corde Vibrante")
plt.show()