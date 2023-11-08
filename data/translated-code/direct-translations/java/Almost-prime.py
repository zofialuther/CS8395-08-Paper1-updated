def main():
    for k in range(1, 6):
        print("k = " + str(k) + ":", end="")
        c = 0
        i = 2
        while c < 10:
            if kprime(i, k):
                print(" " + str(i), end="")
                c += 1
            i += 1
        print("")

def kprime(n, k):
    f = 0
    p = 2
    while f < k and p * p <= n:
        while n % p == 0:
            n //= p
            f += 1
        p += 1
    return f + (1 if n > 1 else 0) == k

if __name__ == "__main__":
    main()