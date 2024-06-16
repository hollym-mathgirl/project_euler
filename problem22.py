import pandas as pd

file_path = 'file path goes here'

with open(file_path, 'r') as file:
    contents = file.read()

names = contents.replace('"', '').split(',')
names.sort()

def words_to_numbers(words):
    def letter_to_number(letter):
        return ord(letter.upper()) - 64
    
    result = []
    for word in words:
        word_numbers = [letter_to_number(letter) for letter in word]
        result.append(word_numbers)
    return result

names_scored = words_to_numbers(names)

total_sum = 0
numbered_names = [(index + 1, name) for index, name in enumerate(names_scored)]
for number, name in numbered_names:
    total = (number * sum(name))
    total_sum += total
print(total_sum)
