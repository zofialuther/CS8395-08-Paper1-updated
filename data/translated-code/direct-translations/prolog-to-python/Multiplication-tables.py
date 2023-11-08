def make_table(S, E):
    print_header(S, E)
    make_table_rows(S, E)
    return

def print_header(S, E):
    print("\n      ", end="")
    for x in range(S, E+1):
        print_num(x)
    print("\n", end="")
    Sp = E * 4 + 2
    print("    ", end="")
    for _ in range(1, Sp+1):
        print("-", end="")
    print("\n", end="")

def make_table_rows(S, E):
    for N in range(S, E+1):
        print("\n", end="")
        print_num(N)
        print(": ", end="")
        for N2 in range(S, E+1):
            X = N * N2
            print_row_item(N, N2, X)

def print_row_item(N, N2, X):
    if N2 < N:
        print("    ", end="")
    elif N2 >= N:
        print_num(X)

def print_num(X):
    if X < 10:
        print(f"   {X}", end="")
    elif 10 <= X <= 99:
        print(f"  {X}", end="")
    elif X > 99:
        print(f" {X}", end="")