from itertools import permutations

def path(List, To, From, [From], W):
    for elem in List:
        if elem[0] == To and elem[1] == From:
            return elem[2]
    return 0

def find_path(Din, From, To, Path, Wout):
    paths = []
    for p in permutations(range(1, 5), 2):
        if p[0] != p[1]:
            P = [p[0]]
            W = path(Din, p[0], p[1], P, 0)
            if W != 0:
                paths.append([W, P])
    paths.sort()
    Wout, Path = paths[0]

def print_all_paths():
    D = [[1, 3, -2], [2, 3, 3], [2, 1, 4], [3, 4, 2], [4, 2, -1]]
    print('Pair\t  Dist\tPath')
    for p in permutations(range(1, 5), 2):
        if p[0] != p[1]:
            Path = []
            Weight = 0
            find_path(D, p[0], p[1], Path, Weight)
            PPath = ' -> '.join(map(str, Path))
            print(f'{p[0]} -> {p[1]}\t  {Weight}\t{PPath}')

print_all_paths()