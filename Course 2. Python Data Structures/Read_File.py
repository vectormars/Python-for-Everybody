#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 21:34:08 2017

@author: jiexue
"""

fname = raw_input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print 'File cannot be opened',fname
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count+1
print 'There were',count,'subject lines in',fname


