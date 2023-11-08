def hanoi(N):
    move(N, 'left', 'center', 'right')

def move(N, A, B, C):
    if N == 0:
        return
    M = N - 1
    move(M, A, C, B)
    inform(A, B)
    move(M, C, B, A)

def inform(X, Y):
    print("move a disk from the " + X + " pole to " + Y + " pole")