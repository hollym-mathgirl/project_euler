squares = []
natural = []

for i in range (1, 101):
    natural.append(i)

for i in range(1, 101):
    squares.append(i*i)

square_of_sum = (sum(natural))**2
sum_of_squares = sum(squares)

answer = square_of_sum - sum_of_squares

print(answer)
