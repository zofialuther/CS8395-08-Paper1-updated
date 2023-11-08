# Python code
with open("data.txt", "r") as file:
    for line in file:
        split = line.split()
        magnitude = float(split[2])
        if magnitude > 6:
            print(line)