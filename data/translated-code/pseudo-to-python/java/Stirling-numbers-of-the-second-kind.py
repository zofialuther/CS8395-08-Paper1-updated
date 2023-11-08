def main():
    print("Stirling numbers of the second kind:")
    max = 12
    print("n/k")
    for n in range(max+1):
        print(n)
    print("")
    for n in range(max+1):
        print(n)
        for k in range(n+1):
            print(sterling2(n, k))
        print("")
    print("The maximum value of S2(100, k) = ")
    previous = 0
    for k in range(1, 101):
        current = sterling2(100, k)
        if current > previous:
            previous = current
        else:
            print(previous)
            print("(%d digits, k = %d)" % (len(str(previous)), k-1))
            break

def sterling2(n, k):
    key = str(n) + "," + str(k)
    if COMPUTED.contains(key):
        return COMPUTED.get(key)
    if (n == 0 and k == 0):
        return 1
    if (n > 0 and k == 0) or (n == 0 and k > 0):
        return 0
    if n == k:
        return 1
    if k > n:
        return 0
    result = k * sterling2(n-1, k) + sterling2(n-1, k-1)
    COMPUTED.put(key, result)
    return result