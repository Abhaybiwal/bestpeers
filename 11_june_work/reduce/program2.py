from functools import reduce

def product_elements(nums):
    return reduce(lambda x, y: x * y, nums)

nums = [1, 2, 3, 4]
print(product_elements(nums)) 
