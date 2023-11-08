def task1():
    for i in range(1, 12):
        F = farey(i)
        print(f'{i}: ', end='')
        rwrite(F)
        print()

def task2():
    for i in range(1, 11):
        I100 = i * 100
        F = farey(I100)
        N = len(F)
        print(f'|F({I100})| = {N}')

# farey(+Order, Sequence)
def farey(Order):
    S = [I/J for J in range(1, Order+1) for I in range(J+1)]
    S.sort()
    return S

def rprint(R):
    if isinstance(R, float):
        A, B = R.as_integer_ratio()
        print(f'{A}/{B}', end='')
    else:
        print(f'{R}/1', end='')

def rwrite(sequence):
    for i, R in enumerate(sequence):
        rprint(R)
        if i < len(sequence) - 1:
            print(', ', end='')

task1()
task2()