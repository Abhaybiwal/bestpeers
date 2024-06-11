from functools import reduce

def flatten_list_of_lists(list_of_lists):
    return reduce(lambda x, y: x + y, list_of_lists)

list_of_lists = [[1, 2], [3, 4], [5, 6]]
print(flatten_list_of_lists(list_of_lists))  
