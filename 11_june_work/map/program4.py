def celsius_to_fahrenheit(celsius):
    return list(map(lambda c: (c * 9/5) + 32, celsius))

celsius = [0, 20, 30, 100]
print(celsius_to_fahrenheit(celsius))  # Output: [32.0, 68.0, 86.0, 212.0]
