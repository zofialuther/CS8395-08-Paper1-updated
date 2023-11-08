def do(V):
    if V == 0:
        print(0)
        print()
        do(1)
    elif V % 6 == 0:
        return
    else:
        print(V)
        print()
        Y = V + 1
        do(Y)

def wloop():
    do(0)