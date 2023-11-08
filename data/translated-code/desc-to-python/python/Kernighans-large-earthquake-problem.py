with open("data.txt", "r") as file:
    for line in file:
        elements = line.split()
        if float(elements[2].strip()) > 6:
            print(line)