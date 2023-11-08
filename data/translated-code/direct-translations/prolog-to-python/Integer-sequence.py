from chr import *

@chr_constraint
def loop(N):
    print(N)
    N1 = N + 1
    loop(N1)