from functools import reduce

def concatenate_strings(strings):
    return reduce(lambda x, y: x + y, strings)

strings = ["Hello", " ", "World", "!"]
print(concatenate_strings(strings))  
