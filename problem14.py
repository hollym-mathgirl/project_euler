collatz_lengths = {}

for n in range(2, 1000000):
    original_n = n
    stops = []
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        stops.append(n)
    
    collatz_lengths[original_n] = len(stops)

max_length = max(collatz_lengths.values())
starting_number = max(collatz_lengths, key=collatz_lengths.get)

print(f"The starting number under one million that produces the longest Collatz chain is {starting_number} with an orbit of {max_length}.")
