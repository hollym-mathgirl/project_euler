import math

def count_divisors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

def find_triangle_number(divisor_limit):
    n = 1
    triangle_number = 0
    while True:
        triangle_number += n
        n += 1
        if count_divisors(triangle_number) > divisor_limit:
            return triangle_number

divisor_limit = 500
print(find_triangle_number(divisor_limit))
