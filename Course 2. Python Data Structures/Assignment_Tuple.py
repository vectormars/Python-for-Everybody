# -*- coding: utf-8 -*-
"""
@author: Jie Xue
"""


s = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
print s.find(':')
print s[s.find(':')-2:s.find(':')]


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)




dict = {}
for line in handle:
    if not line.startswith('From'):
        continue
    hour = line[line.find(':')-2:line.find(':')]
    if not hour.isdigit():
        continue
    if hour not in dict:
        dict[hour] = 1
    else:
        dict[hour] = dict[hour]+1
            
for key in sorted(dict):
    print "%s %s" % (key, dict[key])