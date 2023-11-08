def main():
    pas(20)

def pas(rows):
    for i in range(rows+1):
        for j in range(i+1):
            print(ncr(i, j), end=" ")
        print("\n")

def ncr(n, r):
    return fact(n) // (fact(r) * fact(n - r))

def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans = ans * i
    return ans