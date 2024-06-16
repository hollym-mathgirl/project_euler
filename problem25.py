def fibonacci(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

x = 1000
counter = 1
output = fibonacci(counter)

while len(str(output)) < x:
    counter += 1
    output = fibonacci(counter)

print(f"The output number with at least {x} digits is: {output}")
print(f"The position in the Fibonacci sequence is: {counter}")
