text = "dog cat dog bird cat dog bird bird"
word_count = {word: text.split().count(word) for word in set(text.split())}
print(word_count)
