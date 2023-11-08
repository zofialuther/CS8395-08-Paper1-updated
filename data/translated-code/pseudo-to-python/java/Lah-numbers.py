def lahNumber(n, k):
    CACHE = {}
    key = str(n) + "," + str(k)
    if key in CACHE:
        return CACHE[key]
    result = 0
    if n == 0 and k == 0:
        result = 1
    elif k == 0:
        result = 0
    elif k > n:
        result = 0
    elif n == 1 and k == 1:
        result = 1
    else:
        result = (n-1+k) * lahNumber(n-1, k) + lahNumber(n-1, k-1)
    CACHE[key] = result
    return result

def main():
    print("Show the unsigned Lah numbers up to n = 12:")
    for n in range(13):
        print(n)
        for k in range(n + 1):
            print(lahNumber(n, k))
    print("Show the maximum value of L(100, k):")
    n = 100
    max_val = 0
    for k in range(n + 1):
        max_val = max(max_val, lahNumber(n, k))
    print(max_val)