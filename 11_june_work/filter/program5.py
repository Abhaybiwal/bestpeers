def filter_numbers_in_range(nums, min_val, max_val):
    return list(filter(lambda x: min_val <= x <= max_val, nums))

nums = [1, 10, 20, 30, 40, 50]
min_val = 15
max_val = 35
print(filter_numbers_in_range(nums, min_val, max_val)) 
