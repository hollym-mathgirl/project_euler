import numpy as np

#initialize a matrix of all zeroes using the numpy zeros function
size = 1001
spiral_matrix = np.zeros((size, size), dtype=int)

#find the center starting point by doing integer division by 2
x, y = size // 2, size // 2
spiral_matrix[x, y] = 1

#directions are defined by (x, y) movements and listed in this order: right down left up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_index = 0

#steps to take in the current direction
steps = 1

#current value to fill in the spiral
current_value = 2

while current_value <= size * size:
    for _ in range(2):
        for _ in range(steps):
            x += directions[direction_index][0]
            y += directions[direction_index][1]
            if 0 <= x < size and 0 <= y < size:
                spiral_matrix[x, y] = current_value
                current_value += 1
        direction_index = (direction_index + 1) % 4
    steps += 1

#calculate the sum of the upper left to lower right diagonal: (1, 1) (2, 2)....
primary_diagonal_sum = sum(spiral_matrix[i, i] for i in range(size))
#calculate the sum of the other diagonal: (1, (end-1-1)), (2, (end-1-2))....
secondary_diagonal_sum = sum(spiral_matrix[i, size - 1 - i] for i in range(size))

#since the center is counted in both diagonals, subtract it once
center_value = spiral_matrix[size // 2, size // 2]
total_diagonal_sum = primary_diagonal_sum + secondary_diagonal_sum - center_value

print(f"Sum of primary diagonal: {primary_diagonal_sum}")
print(f"Sum of secondary diagonal: {secondary_diagonal_sum}")
print(f"Total sum of both diagonals: {total_diagonal_sum}")
