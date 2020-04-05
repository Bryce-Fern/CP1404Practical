words = {}
text = {"This is a collection"}
print(text)

check_for_word = text.split()
for word in check_for_word:
    frequency = words.get(word, 0)
    words[word] = frequency + 1