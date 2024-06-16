def fibonacci_sum_even(limit):
    a, b = 1, 2
    total = 0
    while b < limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

print(fibonacci_sum_even(4000000))
