def filter_even_numbers(nums):
    return list(filter(lambda x: x % 2 == 0, nums))

nums = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(nums))
