def doors_optimized(N):
    Max = int(N ** 0.5)
    for i in range(1, Max+1):
        print(f"The door {i*i} is open")