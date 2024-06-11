from functools import reduce

def max_element(nums):
    return reduce(lambda x, y: x if x > y else y, nums)

nums = [1, 3, 5, 2, 4]
print(max_element(nums))  
