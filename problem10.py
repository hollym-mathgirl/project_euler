def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * limit
    sieve[0] = sieve[1] = False 

    for i in range(2, limit):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, limit, i):
                sieve[j] = False
    return primes

limit = 2000000
primes = sieve_of_eratosthenes(limit)
result = sum(primes)

print(f"The sum of all primes below {limit} is: {result}")
