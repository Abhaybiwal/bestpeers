def filter_words_starting_with(words, letter):
    return list(filter(lambda w: w.startswith(letter), words))

words = ["apple", "banana", "cherry", "apricot"]
letter = "a"
print(filter_words_starting_with(words, letter)) 
