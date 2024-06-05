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
        
print(flaten(nested_list))

