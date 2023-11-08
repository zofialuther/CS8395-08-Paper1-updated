import os

def isEmpty(x):
    contents = os.listdir(x)
    if len(contents) == 2:
        return "Directory is empty"
    else:
        return "Directory is not empty"

def main():
    args = os.sys.argv
    directory = args[1]
    result = isEmpty(directory)
    print(result)

main()