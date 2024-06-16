def get_prime_decomposition(n):
    prime_factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors

number = 600851475143
prime_factors = get_prime_decomposition(number)
print("Prime factors are: ", prime_factors)
