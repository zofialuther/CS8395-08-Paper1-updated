def MultiplicationTable():
    for i in range(1, 13):
        print("\t" + str(i), end="")
    print("\n")
    for i in range(0, 101):
        print("-", end="")
    print("\n")
    for i in range(1, 13):
        print(str(i) + "|", end="")
        for j in range(1, 13):
            print("\t", end="")
            if j >= i:
                print("\t" + str(i * j), end="")
        print("\n")