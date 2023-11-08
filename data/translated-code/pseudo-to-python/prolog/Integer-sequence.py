from constraint import chr

@chr
def loop(N):
    print(N)
    N1 = N + 1
    loop(N1)