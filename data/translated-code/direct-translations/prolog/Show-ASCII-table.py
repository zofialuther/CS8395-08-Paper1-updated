def ascii():
    for n in range(32, 48):
        row(n)

def row(n):
    if n > 127:
        print("\n")
    else:
        code(n)
        ascii(n)
        nn = n + 16
        row(nn)

def code(n):
    if n < 100:
        print(f'  {n} : ', end='')
    else:
        print(f' {n} : ', end='')

def ascii(n):
    if n == 32:
        print(' Spc    ', end='')
    elif n == 127:
        print(' Del   ', end='')
    else:
        d = chr(n)
        print(f' {d}      ', end='')

ascii()