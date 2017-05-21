"""
@author: jiexue
"""

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

def get_num(text):
    pos = text.find(':')
    text_num=text[pos+1:len(text)].strip()
    return float(text_num)
    
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    total = total + get_num(line)
    count = count +1
   
print 'Average spam confidence:',total/count