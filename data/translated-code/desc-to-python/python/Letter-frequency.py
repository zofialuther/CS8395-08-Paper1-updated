import sys
import collections

def filecharcount(file):
    content = file.read()
    counter = collections.Counter(content)
    return sorted(counter.items())

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        result = filecharcount(file)
        print(result)