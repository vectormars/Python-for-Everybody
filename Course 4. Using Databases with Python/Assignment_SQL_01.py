# -*- coding: utf-8 -*-
"""
@author: Jie Xue
"""

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')


fname = 'mbox.txt'
try:
    fh = open(fname)
except:
    print 'File cannot be opened',fname
    exit()

organizationDict = {}
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.rstrip().split('@')
    organization = pieces[1]
    if organization not in organizationDict:
        organizationDict[organization] = 1
    else:
        organizationDict[organization] = organizationDict[organization]+1

for key in sorted(organizationDict, key=organizationDict.get):
    cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, ? )''', ( key, int(organizationDict[key])) )
    print key
    print organizationDict[key]
#    print "%s %d" % (key, organizationDict[key])

conn.commit() 



cur.close()