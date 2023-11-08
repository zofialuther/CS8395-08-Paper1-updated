```python
def hamming(N):
    global go
    go = 1
    if N == 20:
        watch_20(20, L)
    else:
        watch(1, N, L)
    
    L = [1, *L235]
    multlist(L, 2, L2)
    multlist(L, 3, L3)
    multlist(L, 5, L5)
    merge_(L2, L3, L23)
    merge_(L5, L23, L235)

def multlist(L, N, XLN):
    global go
    if go == 1:
        if len(L) > 0:
            X = L[0]
            if not str(X).isalpha():
                XN = X * N
                XLN = [XN, *LN]
                multlist(L[1:], N, LN)
                

def merge_(In1, In2, XYOut):
    global go
    if go == 1:
        if len(In1) > 0 and len(In2) > 0:
            X = In1[0]
            Y = In2[0]
            if X < Y:
                XYOut = [X, *Out]
                merge_(In1[1:], In2, Out)
            elif X == Y:
                XYOut = [X, *Out]
                merge_(In1[1:], In2, Out)
            else:
                XYOut = [Y, *Out]
                merge_(In1, In2[1:], Out)

def watch(Max, N, L):
    global go
    if N == Max:
        if not str(L[0]).isalpha():
            print(L[0])
            go = 0
    else:
        watch(N + 1, Max, L[1:])

def watch_20(N, L):
    global go
    if N == 1:
        if not str(L[0]).isalpha():
            print(L[0])
            go = 0
    else:
        if not str(L[0]).isalpha():
            print(str(L[0]) + " ")
            watch_20(N - 1, L[1:])
```