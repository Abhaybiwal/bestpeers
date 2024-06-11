def filter_positive_numbers(nums):
    return list(filter(lambda x: x > 0, nums))

nums = [-1, 2, -3, 4, -5, 6]
print(filter_positive_numbers(nums))
