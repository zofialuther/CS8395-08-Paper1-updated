from itertools import combinations_with_replacement

# Define the list of items and the value of k
n = 'iced jam plain'.split()
k = 2

# Use the combinations_with_replacement function to generate combinations
combinations = list(combinations_with_replacement(n, k))
print(combinations)

# Extra credit
extra_credit_combinations = list(combinations_with_replacement(range(10), 3))
print(len(extra_credit_combinations))