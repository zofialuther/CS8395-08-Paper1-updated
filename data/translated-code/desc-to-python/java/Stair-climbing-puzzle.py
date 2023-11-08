def stepUp():
    i = 0
    for _ in range(1):
        if step():
            i += 1
        else:
            i -= 1
        if i < 1:
            break