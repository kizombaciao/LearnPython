import itertools

my_list = [1, 2, 3, 4, 5, 6]

combinations = itertools.combinations(my_list, 3)
permutations = itertools.permutations(my_list, 3)

#print([result for result in combinations if sum(result) == 10])

print([result for result in permutations if sum(result) == 10])
