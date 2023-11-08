def nth(N, N_Th):
    if tween(N):
        Th = "th"
    elif 1 == N % 10:
        Th = "st"
    elif 2 == N % 10:
        Th = "nd"
    elif 3 == N % 10:
        Th = "rd"
    else:
        Th = "th"
    return str(N) + Th + str(N_Th)

def tween(N):
    Tween = N % 100
    return 11 <= Tween <= 13

def test():
    for N in range(0, 25):
        print(nth(N, N))
    print("\n")
    for N in range(250, 265):
        print(nth(N, N))
    print("\n")
    for N in range(1000, 1025):
        print(nth(N, N))