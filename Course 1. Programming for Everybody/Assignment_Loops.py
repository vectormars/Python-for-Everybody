#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:42:27 2017

@author: jiexue
"""

largest = None
smallest = None
while True:
    inp = raw_input('Enter a number: ')
    
    if inp == 'done':
        break
    if len(inp) < 1:
        break
    
    try:
        num = float(inp)
    except:
        print "Invalid input"
        
        
    if (num > largest) | (largest is None):
        largest = num
          
    if (num < smallest) | (smallest is None):
        smallest=num

print "Maximum is", int(largest)
print "Minimum is", int(smallest)