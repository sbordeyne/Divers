# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:48:04 2015

@author: Simon
"""

def func():  
   print ('Calling func only this time')
   func.__code__ = (lambda:None).__code__  
   pass
