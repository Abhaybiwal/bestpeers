def sort_tuples_by_second_element(tuples):
    return sorted(tuples, key=lambda x: x[1])

tuples = [(1, 3), (3, 1), (2, 2)]
print(sort_tuples_by_second_element(tuples)) 