def add_lists(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
print(add_lists(list1, list2))  # Output: [11, 22, 33, 44]
