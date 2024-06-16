import itertools
input_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
permutations = itertools.permutations(input_tuple)
permutations_list = list(permutations)
print(permutations_list[999999])
