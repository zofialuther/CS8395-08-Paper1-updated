from itertools import combinations

def lis(arr):
    return max((list(seq) for seq in combinations(arr, len(arr)) if seq == sorted(seq, key=lambda x: (x,))) or [[]], key=len)

print(lis([3,2,6,4,5,1]))
print(lis([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]))
print(lis([1,1,1,1]))