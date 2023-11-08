import sys

if len(sys.argv) < 2:
    print("Usage: python program_name.py input_file")
else:
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        for line in file:
            if "#" in line:
                line = line.split("#")[0]
            if ";" in line:
                line = line.split(";")[0]
            print(line)