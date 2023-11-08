def evens(D, Es):
    Es = []
    for E in D:
        if E % 2 == 0:
            Es.append(E)
    return Es