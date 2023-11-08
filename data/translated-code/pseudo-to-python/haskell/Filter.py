from Data.Array import *
ary = listArray(1, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
n = len(ary)
l = [ary[i] for i in range(1, n+1) if ary[i] % 2 == 0]
evens = listArray(1, n, l)