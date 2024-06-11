def filter_long_strings(strings, min_length):
    return list(filter(lambda s: len(s) > min_length, strings))

strings = ["apple", "banana", "cherry", "date"]
min_length = 5
print(filter_long_strings(strings, min_length))  # Output: ['banana', 'cherry']
