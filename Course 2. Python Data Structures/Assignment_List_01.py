"""
@author: jiexue
"""

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
	words = line.rstrip().split()
    
        for word in words:
            if word not in lst:
                lst.append(word)
              
lst.sort()
print lst


"""
Desired Output:
    
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
"""