# -*- coding: utf-8 -*-
"""
http://python-data.dr-chuck.net/known_by_Fikret.html 
@author: Jie Xue
"""


import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

k = 0
while k<=3:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    tags = soup('a')
    i = 0
    for tag in tags:
        i = i + 1
        if (i == 3):
            print tag.get('href', None)
            url = tag.get('href', None)
            break
    k = k +1
  

"""
Desired Output:
    
Enter URL: http://python-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://python-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://python-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://python-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://python-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://python-data.dr-chuck.net/known_by_Anayah.html
"""    