from itertools import permutations

def path(List, To, From, [From], W):
    for item in List:
        if item[0] == To and item[1] == From:
            W = item[2]
            return

def path(List, To, From, [Link, *R], W):
    for item in List:
        if item[0] == To and item[1] == Link:
            W1 = item[2]
            Rest = List.remove(item)
            W = W1 + W2
            path(Rest, Link, From, R, W2)

def find_path(Din, From, To, [From, *Pout], Wout):
    for i in range(1, 5):
        for j in range(1, 5):
            if i != j:
                paths = []
                for item in Din:
                    if item[0] == From and item[1] == To:
                        P = [item[2]]
                        W = item[2]
                        paths.append([W,P])
                paths.sort()
                Wout, Pout = paths[0]

def print_all_paths():
    D = [[1, 3, -2], [2, 3, 3], [2, 1, 4], [3, 4, 2], [4, 2, -1]]
    print('Pair\t  Dist\tPath\n')
    for item in permutations(range(1, 5), 2):
        From, To = item
        Path = []
        Weight = 0
        find_path(D, From, To, Path, Weight)
        PPath = ' -> '.join(str(x) for x in Path)
        print(f'{From} -> {To}\t  {Weight}\t{PPath}\n')
```