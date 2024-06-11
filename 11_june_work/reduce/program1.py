from functools import reduce

def sum_elements(nums):
    return reduce(lambda x, y: x + y, nums)

nums = [1, 2, 3, 4, 5]
print(sum_elements(nums)) 
