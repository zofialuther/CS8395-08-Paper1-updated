import collections
import sys

def filecharcount(openfile):
    return sorted(collections.Counter(char for line in openfile for char in line).items())

with open(sys.argv[1], 'r') as file:
    print(filecharcount(file))