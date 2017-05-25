# -*- coding: utf-8 -*-
"""
http://python-data.dr-chuck.net/comments_42.json
@author: Jie Xue
"""

import json
import urllib

url = raw_input('Enter location: ')
data = urllib.urlopen(url).read()

info = json.loads(str(data))
Keys = info.keys()

i = 0
List = list()
while i<len(info[Keys[1]]):
    print info['comments'][i]['count']
    List.append(int(info['comments'][i]['count']))
    i = i + 1
    
print List
print sum(List)

"""
Desired Output: 2553
"""