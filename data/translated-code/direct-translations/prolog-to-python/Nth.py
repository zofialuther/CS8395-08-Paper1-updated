def nth(N, N_Th):
    if tween(N):
        Th = "th"
    elif N % 10 == 1:
        Th = "st"
    elif N % 10 == 2:
        Th = "nd"
    elif N % 10 == 3:
        Th = "rd"
    else:
        Th = "th"
    N_Th = str(N) + Th

def tween(N):
    Tween = N % 100
    return 11 <= Tween <= 13

def test():
    for N in range(0, 26):
        nth(N, N_Th)
        print(N_Th, end=", ")
    print("\n")
    
    for N in range(250, 266):
        nth(N, N_Th)
        print(N_Th, end=", ")
    print("\n")
    
    for N in range(1000, 1026):
        nth(N, N_Th)
        print(N_Th, end=", ")
    print("\n")