from itertools import permutations

def isSolution(arr):
    a, b, c, d, e, f, g, h = arr
    differences = [
        abs(a - d),
        abs(c - d),
        abs(g - d),
        abs(e - d),
        abs(a - c),
        abs(c - g),
        abs(g - e),
        abs(e - a),
        abs(b - e),
        abs(d - e),
        abs(h - e),
        abs(f - e),
        abs(b - d),
        abs(d - h),
        abs(h - f),
        abs(f - b)
    ]
    return all(diff > 1 for diff in differences)

solution = next(filter(isSolution, permutations(range(1, 9))))

print('A =', solution[0])
print('B =', solution[1])
print('C =', solution[2])
print('D =', solution[3])
print('E =', solution[4])
print('F =', solution[5])
print('G =', solution[6])
print('H =', solution[7])