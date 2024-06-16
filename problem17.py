from num2words import num2words

words = []

for i in range(1, 1001):
    word = num2words(i)
    words.append(word)

#this module counts both commas and spaces, so they must be replaced before counting
total_characters = sum(len(word.replace('-', '').replace(' ', '').replace(',', '')) for word in words)

print(f"The total number of characters in all words is {total_characters}.")
