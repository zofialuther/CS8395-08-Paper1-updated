def task_1():
    for I in range(1, 12):
        F = farey(I)
        print(str(I) + ': ' + str(F))

def task_2():
    for I in range(1, 11):
        I100 = I * 100
        F = farey(I100)
        N = len(F)
        print('|F(' + str(I100) + ')| = ' + str(N))

def farey(Order):
    S = [I/J for J in range(1, Order+1) for I in range(0, J)]
    Sequence = sorted(S)
    return Sequence

def rprint(r):
    if isinstance(r, tuple):
        print(str(r[0]) + '/' + str(r[1]))
    else:
        if isinstance(r, int):
            print(str(r) + '/1')

def rwrite(sequence):
    if len(sequence) == 0:
        return
    elif len(sequence) == 1:
        rprint(sequence[0])
    else:
        rprint(sequence[0])
        print(', ', end='')
        rwrite(sequence[1:])

def rcompare(A, B):
    if A < B:
        return True
    elif A > B:
        return True
    elif A <= B:
        return True