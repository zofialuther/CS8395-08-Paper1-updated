from functools import cmp_to_key
from itertools import permutations

def compare(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    return (ba > ab) - (ab > ba)

def largest_number(arr):
    sorted_arr = sorted(arr, key=cmp_to_key(compare))
    return ''.join(map(str, sorted_arr))

ints1 = [1, 34, 3, 98, 9, 76, 45, 4]
ints2 = [54, 546, 548, 60]

print(largest_number(ints1))
print(largest_number(ints2))