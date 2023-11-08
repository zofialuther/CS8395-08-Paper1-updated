from itertools import permutations

dinesman = []
for perm in permutations([1, 2, 3, 4, 5]):
    baker, cooper, fletcher, miller, smith = perm
    if baker != 5 and cooper != 1 and (fletcher != 5 and fletcher != 1) and miller > cooper and abs(smith - fletcher) != 1 and abs(fletcher - cooper) != 1:
        dinesman.append((baker, cooper, fletcher, miller, smith))

print(dinesman[0])
print(dinesman)