"""
@author: Jie Xue
"""
import re

fname = raw_input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print 'File cannot be opened',fname
    exit()

List = []
for line in fhand:
    nums = re.findall('[0-9]+',line)
    if nums:
        i = 0
        while i < len(nums):
            List.append(nums[i])
            i = i +1
print len(List)

print List

total = sum(map(int, List))
print "Total",total
