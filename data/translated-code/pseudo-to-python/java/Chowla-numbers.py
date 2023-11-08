def main():
    chowlaNumbers = findChowlaNumbers(37)
    for i in range(len(chowlaNumbers)):
        print("chowla(" + str(i+1) + ") = " + str(chowlaNumbers[i]))
    
    primes = countPrimes(100, 10_000_000)
    for i in range(len(primes)):
        print("There is " + str(primes[i][1]) + " primes up to " + str(primes[i][0]))
    
    perfectNumbers = findPerfectNumbers(35_000_000)
    for i in range(len(perfectNumbers)):
        print(str(perfectNumbers[i]) + " is a perfect number")
    print("There are " + str(len(perfectNumbers)) + " perfect numbers < 35,000,000")

def chowla(n):
    if n < 0:
        raise ValueError("n is not positive")
    sum = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            sum += i + (i if (j := n // i) == i else j)
    return sum

def countPrimes(power, limit):
    count = 0
    num = [[0, 0] for _ in range(countMultiplicity(limit, power))]
    for n in range(2, limit+1):
        if chowla(n) == 0:
            count += 1
        if n % power == 0:
            num[count][0] = power
            num[count][1] = count
            count += 1
            power *= 10
    return num

def countMultiplicity(limit, start):
    count = 0
    cur = limit
    while cur >= start:
        count += 1
        cur = cur // 10
    return count

def findChowlaNumbers(limit):
    num = [0] * limit
    for i in range(limit):
        num[i] = chowla(i+1)
    return num

def findPerfectNumbers(limit):
    count = 0
    num = [0] * count

    k = 2
    kk = 3
    p = 0
    while (p := k * kk) < limit:
        if chowla(p) == p - 1:
            num = increaseArr(num)
            num[count] = p
            count += 1
        k = kk + 1
        kk += k
    return num

def increaseArr(arr):
    tmp = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        tmp[i] = arr[i]
    return tmp