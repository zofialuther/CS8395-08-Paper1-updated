from functools import lru_cache

@lru_cache(maxsize=None)
def stirling1(n, k):
    if k == 0:
        return 0
    elif n == 0 and k > 0:
        return 0
    elif k > n:
        return 0
    else:
        return (n-1)*stirling1(n-1, k) + stirling1(n-1, k-1)

def main():
    print("n/k |", end="")
    for k in range(13):
        print(f" {k} |", end="")
    print("\n" + "-"*40)
    for n in range(13):
        print(f"{n}   |", end="")
        for k in range(13):
            print(f" {stirling1(n, k)} |", end="")
        print()
    
    max_val = max(stirling1(100, k) for k in range(101))
    print(f"The maximum value of S1(100, k) is {max_val}")

main()