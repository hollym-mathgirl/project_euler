x = 1000  #desired number of digits

#initializing first two Fibonacci numbers
a, b = 1, 1
counter = 2  #starting from the 3rd Fibonacci number

while len(str(b)) < x:
    a, b = b, a + b
    counter += 1

print(f"The output number with at least {x} digits is: {b}")
print(f"The position in the Fibonacci sequence is: {counter}")

