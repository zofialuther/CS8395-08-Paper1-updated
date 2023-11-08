def ludic():
    sequence = list(range(1, 20000))
    n = 2
    while len(sequence) > 10000:
        sequence = [x for i, x in enumerate(sequence, 1) if i % n != 0]
        n += 1
    print(sequence[-1])

ludic()