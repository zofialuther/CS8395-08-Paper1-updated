for i in range(1, 11):
    print(i, end="")
    if i % 5 == 0:
        print("\n")
        continue
    print(", ", end="")