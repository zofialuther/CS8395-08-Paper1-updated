```python
import threading

def hamming(N):
    def watch_20(n, l):
        if n == 1:
            if isinstance(l[0], int):
                print(l[0])
                go = 0
        else:
            if isinstance(l[0], int):
                print(l[0], end=' ')
                watch_20(n - 1, l[1:])

    def watch(n, max, l):
        if n == max:
            if isinstance(l[0], int):
                print(l[0])
                go = 0
        else:
            if isinstance(l[0], int):
                print(l[0])
                watch(n + 1, max, l[1:])

    def multlist(l, n):
        if go == 1:
            if isinstance(l[0], int):
                x_n = l[0] * n
                ln = [x_n]
                multlist(l[1:], n)
        else:
            return

    def merge_(in1, in2):
        if go == 1:
            x, in1 = in1[0], in1[1:]
            y, in2 = in2[0], in2[1:]
            if x < y:
                out = [x]
                in11, in12 = in1, [y] + in2
            elif x == y:
                out = [x]
                in11, in12 = in1, in2
            else:
                out = [y]
                in11, in12 = [x] + in1, in2
            threading.Thread(target=merge_, args=(in11, in12, out)).start()
        else:
            return

    go = 1
    if N == 20:
        watch_20(20, [1])
    else:
        watch(1, N, [1])

    L = [1]
    L235 = []
    multlist(L, 2)
    multlist(L, 3)
    multlist(L, 5)
    merge_(L2, L3)
    merge_(L5, L23)
```