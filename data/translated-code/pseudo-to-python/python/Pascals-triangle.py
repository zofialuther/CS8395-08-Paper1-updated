def pascal(n):
    row = [1]
    k = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [l + r for l, r in zip(row + k, k + row)]
    if n >= 1:
        return True
    else:
        return False