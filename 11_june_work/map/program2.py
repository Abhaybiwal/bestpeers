def to_uppercase(strings):
    return list(map(lambda s: s.upper(), strings))

strings = ["apple", "banana", "cherry"]
print(to_uppercase(strings))  # Output: ['APPLE', 'BANANA', 'CHERRY']
