def find_pythagorean_triplet(sum_total):
    for m in range(2, int(sum_total**0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if a + b + c == sum_total:
                    return a, b, c
                #check for non-primitive pythagorean triplets
                k = sum_total // (a + b + c)
                if k * (a + b + c) == sum_total:
                    return k * a, k * b, k * c
    return None

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

triplet = find_pythagorean_triplet(1000)
if triplet:
    a, b, c = triplet
    print(f"The Pythagorean triplet is: a = {a}, b = {b}, c = {c}")
    print(f"The product abc is: {a * b * c}")
else:
    print("No Pythagorean triplet found with the given sum.")
