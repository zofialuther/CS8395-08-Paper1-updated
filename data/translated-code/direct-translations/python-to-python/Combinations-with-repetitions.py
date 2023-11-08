from itertools import combinations_with_replacement

n, k = 'iced jam plain'.split(), 2
print(list(combinations_with_replacement(n,k)))

# Extra credit
print(len(list(combinations_with_replacement(range(10), 3)))