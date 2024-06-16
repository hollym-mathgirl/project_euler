import math

#this uses combinatorics instead of brute force
def number_of_routes(grid_size):
    return math.comb(2 * grid_size, grid_size)

grid_size = 20
print(number_of_routes(grid_size))
