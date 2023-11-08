```python
def main():
    make_graph()
    Pn = []
    hamiltonian(5*3, Pn)
    show_path(Pn)

def board_size(N):
    return N

def in_board(X, Y):
    N = board_size(8)
    return 1 <= Y <= N and 1 <= X <= N

def make_graph():
    for P in [(X, Y) for X in range(1, 9) for Y in range(1, 9)]:
        assert_moves(P)

def assert_moves(P):
    for Q in [(X1, Y1) for X, Y in [(one(X), two(Y)), (two(X), one(Y))] for X1, Y1 in [(X + 2, Y), (X - 2, Y), (X, Y + 2), (X, Y - 2)] if in_board(X1, Y1)]:
        asserta(move(P, Q))

def one(M, N):
    return (M, N+1) if M < N else (N, M+1)

def two(M, N):
    return (M + 2, N) if M + 2 == N else (M - 2, N)

def hamiltonian(P, Pn):
    N = board_size(8)
    Size = N * N
    Ps = []
    hamiltonian(P, Size, Ps, Pn)

def enumerate(N, Ps, Pn):
    if not Ps:
        return []
    else:
        return [(N, P) for P in Ps] + enumerate(N-1, Ps, Pn)

def hamiltonian(P, N, Ps, Res):
    if N == 1:
        Res = [P] + Ps
    else:
        Q = warnsdorff(Ps, P)
        M = N - 1
        hamiltonian(Q, M, [P] + Ps, Res)

def warnsdorff(Ps, P):
    Qs = [Q for Q in moves(Ps, P) if Q not in Ps]
    Xs = [(len(moves(Ps, Q)), Q) for Q in Qs]
    Ys = sorted(Xs, key=lambda x: x[0])
    return [_, Q] in Ys

def next_moves(Ps, Q, L, Q):
    Rs = moves(Ps, Q)
    L = len(Rs)

def moves(Ps, P, Qs):
    Qs = [Q for Q in [(X1, Y1) for X, Y in [(one(P[0]), two(P[1])), (two(P[0]), one(P[1]))] for X1, Y1 in [(X + 2, Y), (X - 2, Y), (X, Y + 2), (X, Y - 2)] if in_board(X1, Y1)] if Q not in Ps]

def show_path(Pn):
    for P in [(X, Y) for X in range(1, 9) for Y in range(1, 9)]:
        show_cell(Pn, P)

def show_cell(Pn, X, Y):
    N = [N for N, P in Pn if P == (X, Y)]
    print(format('%3.0d' % N), end='')
    print()
```