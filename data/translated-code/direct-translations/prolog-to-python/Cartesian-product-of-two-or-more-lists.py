def product(A, Bs):
    if not A:
        return []
    else:
        B = Bs[0]
        return [A[0], B] if B in Bs else product(A[1:], Bs)

def product_recursive(As, Bs):
    if not As:
        return []
    else:
        return product(As, Bs) + product_recursive(As[1:], Bs)