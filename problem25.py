x = 1000  # The number of digits we are looking for

# Initializing the first two Fibonacci numbers
a, b = 1, 1
counter = 2  # We start from the 3rd Fibonacci number

while len(str(b)) < x:
    a, b = b, a + b
    counter += 1

print(f"The output number with at least {x} digits is: {b}")
print(f"The position in the Fibonacci sequence is: {counter}")

