# Given a List, extract all elements whose frequency is greater than K.
from collections import defaultdict 

def extract(list_elem,k):

    defaul=defaultdict(int)

    for i in list_elem:
        defaul[i]+=1

    for i in defaul:
        if defaul[i] > k:
            print(i)

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K=3
extract(test_list,K)