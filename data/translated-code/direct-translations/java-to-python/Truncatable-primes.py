from math import sqrt

MAX = 1000000
primeList = [True] * (MAX // 2)

sqroot = int(sqrt(MAX))
primeList[0] = False
for num in range(3, sqroot + 1, 2):
    if primeList[num // 2]:
        inc = num * 2
        for factor in range(num * num, MAX, inc):
            primeList[factor // 2] = False

rightTrunc = -1
leftTrunc = -1
for prime in range(MAX - 1 | 1, 2, -2):
    if primeList[prime // 2]:
        if rightTrunc == -1:
            right = prime
            while right > 0 and right % 2 != 0 and primeList[right // 2]:
                right //= 10
            if right == 0:
                rightTrunc = prime
        
        if leftTrunc == -1:
            left = str(prime)
            if '0' not in left:
                while len(left) > 0:
                    iLeft = int(left)
                    if not primeList[iLeft // 2]:
                        break
                    left = left[1:]
                if len(left) == 0:
                    leftTrunc = prime
        
        if leftTrunc != -1 and rightTrunc != -1:
            break

print("Left Truncatable : ", leftTrunc)
print("Right Truncatable : ", rightTrunc)