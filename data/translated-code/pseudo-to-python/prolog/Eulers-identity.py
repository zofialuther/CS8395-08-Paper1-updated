def reduce(A, C):
    B = simplify(A)
    if B == A:
        C = A
    else:
        print("= ", B)
        reduce(B, C)

def simplify(expression):
    if expression == "exp(i*X)":
        return "cos(X) + i*sin(X)"
    elif expression == "0 + A":
        return "A"
    elif expression == "A + 0":
        return "A"
    elif expression == "A + B" and isinstance(A, int) and isinstance(B, int):
        return A + B
    elif expression == "A + B":
        return simplify(A) + simplify(B)
    elif expression == "0 * _":
        return 0
    elif expression == "_ * 0":
        return 0
    elif expression == "1 * A":
        return A
    elif expression == "A * 1":
        return A
    elif expression == "A * B" and isinstance(A, int) and isinstance(B, int):
        return A * B
    elif expression == "A * B":
        return simplify(A) * simplify(B)
    elif expression == "cos(0)":
        return 1
    elif expression == "sin(0)":
        return 0
    elif expression == "cos(pi)":
        return -1
    elif expression == "sin(pi)":
        return 0
    else:
        return expression