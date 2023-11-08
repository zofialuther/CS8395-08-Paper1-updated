from collections import defaultdict

def fizzbuzz(n, mods):
    res = defaultdict(str)
    for num, name in mods:
        for i in range(num, n+1, num):
            res[i] += name
    return '\n'.join(res[i] or str(i) for i in range(1, n+1))

if __name__ == '__main__':
    n = int(input())
    mods = []
    while len(mods) != 3:
        try:
            line = input()
        except EOFError:
            break
        idx = line.find(' ')
        num, name = int(line[:idx]), line[idx+1:]
        mods.append((num, name))
    print(fizzbuzz(n, mods))