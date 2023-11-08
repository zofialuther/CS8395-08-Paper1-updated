from math import sqrt

MAX = 1000000
primeList = [True] * (MAX >> 1)

sqroot = int(sqrt(MAX))
primeList[0] = False
for num in range(3, sqroot + 1, 2):
    if primeList[num >> 1]:
        inc = num << 1
        for factor in range(num * num, MAX, inc):
            primeList[factor >> 1] = False

rightTrunc, leftTrunc = -1, -1
for prime in range((MAX - 1) | 1, 2, -2):
    if primeList[prime >> 1]:
        if rightTrunc == -1:
            right = prime
            while right > 0 and right % 2 != 0 and primeList[right >> 1]:
                right //= 10
            if right == 0:
                rightTrunc = prime
        
        if leftTrunc == -1:
            left = str(prime)
            if '0' not in left:
                while len(left) > 0:
                    iLeft = int(left)
                    if not primeList[iLeft >> 1]:
                        break
                    left = left[1:]
                if len(left) == 0:
                    leftTrunc = prime
        
        if leftTrunc != -1 and rightTrunc != -1:
            break

print("Left  Truncatable : ", leftTrunc)
print("Right Truncatable : ", rightTrunc)