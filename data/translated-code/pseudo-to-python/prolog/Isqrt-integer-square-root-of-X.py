def pow4gtx(X, Q):
    if pow4gtx_helper(X, 1, Q):
        return Q

    if X < A:
        Q = A

    A1 = A * 4
    pow4gtx(X, A1, Q)

def pow4gtx_helper(X, A, Q):
    # implementation of pow4gtx_helper function

def isqrt(X, R):
    if isqrt_helper(X, R, _):
        return

    Q = pow4gtx(X, Q)
    isqrt(X, Q, 0, X, R, Z)

    if _ == 1 and R0 == Z0:
        R = R0
        Z = Z0

    Q1 = Q // 4
    T = Z0 - R0 - Q1
    if T >= 0:
        R1 = R0 // 2 + Q1
        isqrt(X, Q1, R1, T, R, Z)
    else:
        R1 = R0 // 2
        isqrt(X, Q1, R1, Z0, R, Z)

def isqrt_helper(X, R, _):
    # implementation of isqrt_helper function

def roots(N):
    roots(0, N)
    if I == N:
        print(R)
    else:
        print(R + " ")
        I = I + 1
        if N < I + 1:
            return
        else:
            roots(I + 1, N)

def rootspow7(N):
    rootspow7(1, N)
    Pow7 = 7 ** I
    R = isqrt(Pow7)
    print("I: ~D, 7^I: ~D, isqrt(7^I): ~D" % (I, Pow7, R))
    I = I + 2
    if N < I + 1:
        return
    else:
        rootspow7(I + 2, N)

def main():
    print("isqrt(i) for 0 <= i <= 65:~2n")
    roots(65)
    print("~3n")
    print("isqrt(7**i) for 1 <= i <= 73, i odd:~2n")
    print("I: ~s, 7^I: ~s, isqrt(7^I): ~s")
    print("-----------------------------------------------------------------------------------------------------------------------------------~n")
    rootspow7(73)
    exit()