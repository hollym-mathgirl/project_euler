import math

def sum_of_digits_in_factorial(n):
    factorial_value = math.factorial(n)
    
    factorial_str = str(factorial_value)
    
    digit_sum = sum(int(digit) for digit in factorial_str)
    
    return digit_sum

number = 100

result = sum_of_digits_in_factorial(number)

print(f"The sum of the digits in {number}! is {result}.")
