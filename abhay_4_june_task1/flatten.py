def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, (list, tuple,set)):  # Check if item is a list or tuple
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested_list = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]
flattened = flatten(nested_list)
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

nested_list = [[1, 2, [3, 4]], [5, 6], [7, (8, 9)]]
flattened = flatten(nested_list)
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
