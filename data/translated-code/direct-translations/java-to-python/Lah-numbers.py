from math import comb

def lah_number(n, k):
    if k == 0:
        return 0
    elif k > n:
        return 0
    elif n == 1 and k == 1:
        return 1
    else:
        return (n-1+k) * lah_number(n-1, k) + lah_number(n-1, k-1)

print("Show the unsigned Lah numbers up to n = 12:")
for n in range(13):
    print(f"{n:5}", end="")
    for k in range(n+1):
        print(f"{lah_number(n, k):12}", end="")
    print()

print("Show the maximum value of L(100, k):")
max_val = max(lah_number(100, k) for k in range(101))
print(max_val)