import itertools

# Part 1
list1 = ['iced', 'jam', 'plain']
combinations1 = list(itertools.combinations_with_replacement(list1, 2))
print(combinations1)

# Part 2
combinations2 = list(itertools.combinations_with_replacement(range(10), 3))
total_combinations = len(combinations2)
print(total_combinations)