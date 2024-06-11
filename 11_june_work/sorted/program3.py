def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x[key])

# Example usage
dicts = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}]
print(sort_dicts_by_key(dicts, 'age'))  # Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]
