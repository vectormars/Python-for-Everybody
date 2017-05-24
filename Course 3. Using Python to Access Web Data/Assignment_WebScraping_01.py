# -*- coding: utf-8 -*-
"""
http://python-data.dr-chuck.net/comments_42.html 
@author: Jie Xue
"""

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

lst  = list()

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs
    num = float(tag.contents[0])
    if num !=[]:
        lst.append(num)


print lst
print "Length",len(lst)
print "Sum",int(sum(lst))


"""
Desired Solution:
Count 50
Sum 2553
"""