import itertools

residents = ['Amy', 'Bob', 'Clara', 'David', 'Eve']

def dinesman(arrangement):
    # conditions for valid arrangement
    # return True or False

permutations = itertools.permutations(residents)
solution_found = False

for perm in permutations:
    if dinesman(perm):
        print("Valid permutation found:", perm)
        solution_found = True
        break

if not solution_found:
    print("No solution found")