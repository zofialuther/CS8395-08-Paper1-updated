from array import array
import time

def partitions(n):
    p = array('q', [0] * (n + 1))
    p[0] = 1
    for i in range(1, n + 1):
        p[i] = 0
        k = 1
        while True:
            j = (k * (3 * k - 1)) // 2
            if j > i:
                break
            if k % 2 == 1:
                p[i] += p[i - j]
            else:
                p[i] -= p[i - j]
            j = j + k
            if j > i:
                break
            if k % 2 == 1:
                p[i] += p[i - j]
            else:
                p[i] -= p[i - j]
            k += 1
    return p[n]

def main():
    start = int(round(time.time() * 1000))
    result = partitions(6666)
    end = int(round(time.time() * 1000))
    print("P(6666) = " + str(result))
    print("elapsed time: " + str(end - start) + " milliseconds")

main()