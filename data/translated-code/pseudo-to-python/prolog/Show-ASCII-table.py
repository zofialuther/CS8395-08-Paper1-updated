def ascii():
    for N in range(32, 48):
        row(N)

def row(N):
    if N > 127:
        print("\n")
        exit
    else:
        code(N)
        ascii(N)
        Nn = N + 16
        row(Nn)

def code(N):
    if N < 100:
        print("  " + str(N) + " : ")
    else:
        print(" " + str(N) + " : ")

def ascii(N):
    if N == 32:
        print(" Spc    ")
        exit
    elif N == 127:
        print(" Del   ")
        exit
    else:
        D = chr(N)
        print(" " + D + "      ")