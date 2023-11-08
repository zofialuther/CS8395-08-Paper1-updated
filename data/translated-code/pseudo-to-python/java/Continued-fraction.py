def calc(f, n):
    temp = 0
    for ni in range(n, 0, -1):
        p = f(ni)
        temp = p[1] / (p[0] + temp)
    return f(0)[0] + temp

def main():
    fList = []
    fList.append(lambda n: [2 if n > 0 else 1, 1])
    fList.append(lambda n: [n if n > 0 else 2, (n - 1) if n > 1 else 1])
    fList.append(lambda n: [6 if n > 0 else 3, int((2 * n - 1) ** 2)])

    for f in fList:
        print(calc(f, 200))