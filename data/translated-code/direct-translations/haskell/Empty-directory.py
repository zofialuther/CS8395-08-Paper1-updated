from os import listdir
from os.path import isfile, join
import sys

def isEmpty(directory):
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    if len(files) == 0:
        return "Directory is empty"
    else:
        return "Directory is not empty"

if __name__ == "__main__":
    args = sys.argv[1:]
    directory = args[0]
    result = isEmpty(directory)
    print(result)