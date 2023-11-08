import itertools

# Generate all possible permutations of numbers from 1 to 7
permutations = list(itertools.permutations(range(1, 8)))

# Filter permutations to find combinations where the sum of three numbers is equal to 12 and the first number is even
filtered_permutations = [p for p in permutations if sum(p[:3]) == 12 and p[0] % 2 == 0]

# Print the permutations that meet the conditions in a formatted table
for perm in filtered_permutations:
    print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format(perm[0], perm[1], perm[2], perm[3], perm[4], perm[5], perm[6]))