import math
from collections import defaultdict

#the answer is the LCM of all the numbers from 1 to 20
#the prime factors under 20 are easy to do with mental arithmetic, but we will use code to solve them in the spirit of the problem

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

def prime_factor_counts(n):
    factors = defaultdict(int)
    i = 2
    while i * i <= n:
        while (n % i) == 0:
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] += 1
    return factors

#dictionary to hold the highest powers of each prime
highest_powers = defaultdict(int)

for i in range(2, 21):
    factor_counts = prime_factor_counts(i)
    for factor, count in factor_counts.items():
        if count > highest_powers[factor]:
            highest_powers[factor] = count

#calculate the final product using the highest powers of each prime factor
final_answer = 1
for factor, power in highest_powers.items():
    final_answer *= factor ** power

print(f'The highest powers of the prime factors are: {highest_powers}')
print(f'The final answer is: {final_answer}')
