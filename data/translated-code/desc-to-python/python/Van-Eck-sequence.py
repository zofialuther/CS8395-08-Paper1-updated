def van_eck():
    sequence = {}
    a = 0
    i = 0
    while True:
        yield a
        if a in sequence:
            a = i - sequence[a]
        else:
            a = 0
        sequence[a] = i
        i += 1

if __name__ == "__main__":
    gen = van_eck()
    for _ in range(10):
        print(next(gen))
    
    for _ in range(991):
        next(gen)
        
    for _ in range(10):
        print(next(gen))