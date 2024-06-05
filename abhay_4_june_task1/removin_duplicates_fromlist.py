# Python – List excluding duplicates
from collections import defaultdict 

li=list('abhaybiwal')
removeDupli=defaultdict(int)
for i in li:
    removeDupli[i]+=1

for i in removeDupli:
    if not removeDupli[i]>1:
        print(i)