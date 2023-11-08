```python
def pow4gtx(X, Q):
    if X < Q:
        return Q
    else:
        return pow4gtx(X, Q*4)

def isqrt(X, R, Z):
    Q = pow4gtx(X)
    return isqrt_helper(X, Q, 0, X, R, Z)

def isqrt_helper(X, Q, R0, Z0, R, Z):
    if Q == 1:
        R = R0
        Z = Z0
    else:
        Q1 = Q // 4
        T = Z0 - R0 - Q1
        if T >= 0:
            R1 = (R0 // 2) + Q1
            isqrt_helper(X, Q1, R1, T, R, Z)
        else:
            R1 = R0 // 2
            isqrt_helper(X, Q1, R1, Z0, R, Z)

def roots(N):
    result = ""
    for i in range(N + 1):
        R = isqrt(i, 0, 0)
        result += str(R) + " " if i < N else str(R)
    return result

def rootspow7(N):
    result = ""
    for i in range(1, N + 1, 2):
        Pow7 = 7 ** i
        R = isqrt(Pow7, 0, 0)
        result += f"{i:<2}{Pow7:<87}{R:<131}\n"
    return result

def main():
    print("isqrt(i) for 0 <= i <= 65:")
    print(roots(65))
    print()
    print("isqrt(7**i) for 1 <= i <= 73, i odd:")
    print("{0:<2}{1:<87}{2:<131}".format("i", "7**i", "isqrt(7**i)"))
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print(rootspow7(73))

if __name__ == "__main__":
    main()
```