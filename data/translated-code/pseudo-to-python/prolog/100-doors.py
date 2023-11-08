def doors_optimized(N):
    Max = int(N**0.5)
    for I in range(1, Max+1):
        J = I * I
        print("Door" + str(J) + " is open")