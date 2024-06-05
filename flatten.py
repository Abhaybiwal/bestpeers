# def flatten(nested):
#     result = []
#     for item in nested:
#         breakpoint()
#         try:
#             result.extend(flatten(item))
#         except:
#             result.append(item)
#     return result

# nested_list = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]
# flattened = flatten(nested_list)
# print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(flattened))
#     return result

nested_list = [[1, 2, [3, 4]], [5, 6], [7, (8, 9)]]

def flaten(nested_list):
    result = []
    index = 0
    nested_len = len(nested_list)

    while index < nested_len:
        current = nested_list[index]
        curr_type=type(current)
        if (curr_type is not int) and isinstance(current, curr_type):
            nested_len += len(current) - 1
            # nested_list[index+1:index+1] = current
        else:
            result.append(current)
        index += 1

    return result
        
print(flaten(nested_list))

