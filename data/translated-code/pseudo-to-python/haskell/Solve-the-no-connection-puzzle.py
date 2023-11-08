from itertools import permutations

def isSolution(arr):
    a, b, c, d, e, f, g, h = arr
    diff = [abs(a - d), abs(c - d), abs(g - d), abs(e - d), abs(a - c), abs(c - g), abs(g - e), abs(e - a), abs(b - e), abs(d - e), abs(h - e), abs(f - e), abs(b - d), abs(d - h), abs(h - f), abs(f - b)]
    return all(i > 1 for i in diff)

permutation_list = list(permutations(range(1, 9)))
solution = next(arr for arr in permutation_list if isSolution(arr))

print('A =', solution[0])
print('B =', solution[1])
print('C =', solution[2])
print('D =', solution[3])
print('E =', solution[4])
print('F =', solution[5])
print('G =', solution[6])
print('H =', solution[7])

print()
print('     ', solution[0:2])
print('  ', solution[2:6])
print('', solution[6:8])