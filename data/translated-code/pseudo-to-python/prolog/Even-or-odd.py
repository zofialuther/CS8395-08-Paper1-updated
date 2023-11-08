def odd(N):
    if N == 0:
        return False
    elif abs(N) & 1 == 0:
        return True
    else:
        return False