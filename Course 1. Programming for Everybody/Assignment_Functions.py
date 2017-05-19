#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:44:00 2017

@author: jiexue
"""

def computepay(h,r):
    if h<40.0:
        return h*r
    else:
        return (h*r*1.5)-(20*r)

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
h = float(hrs)
r = float(rate)

p = computepay(h,r)
print "Pay",p
