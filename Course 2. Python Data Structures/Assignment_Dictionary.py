"""
Jie Xue
"""

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


dict = {}
for line in handle:
    if not line.startswith('From:'):
        continue
    words = line.rstrip().split()
    email = words[1]
    if email not in dict:
        dict[email] = 1
    else:
        dict[email] = dict[email]+1

    
largest_count = None
largest_email = None
for email,count in dict.items():
    if largest_count is None or count > largest_count:
        largest_count = count
        largest_email = email
print largest_email,largest_count