import sys

if len(sys.argv) == 1:
    print("Usage: python StripLineComments.py StringToProcess")
else:
    inputFile = sys.argv[1]
    input = ""
    try:
        with open(inputFile, 'r') as file:
            for line in file:
                print(line.split("#")[0].split(";")[0])
    except Exception as e:
        print(e)