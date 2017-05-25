# -*- coding: utf-8 -*-
"""
http://python-data.dr-chuck.net/comments_42.xml 
@author: Jie Xue
"""

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
data = urllib.urlopen(url).read()
tree = ET.fromstring(data)


counts = tree.findall('.//comment')

List = list()
for item in counts:
    print 'count', item.find('count').text
    List.append(int(item.find('count').text))
print List
print sum(List)

"""
Desired Output:

2553
"""