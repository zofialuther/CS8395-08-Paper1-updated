with open("data.txt", "r") as f:
    for line in f:
        if float(line.strip().split()[2]) > 6:
            print(line.strip())