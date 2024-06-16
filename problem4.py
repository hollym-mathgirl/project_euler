palindromes = []

def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]

for i in range(900, 1000):
    for j in range(900, 1000):
        product = i * j        
        if is_palindrome(product):
            palindromes.append(product)

print(max(palindromes))
