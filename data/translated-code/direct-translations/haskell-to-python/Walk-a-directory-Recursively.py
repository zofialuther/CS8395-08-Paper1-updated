import os
import sys
import fnmatch

def search(pat, dir):
    matches = []
    for root, dirnames, filenames in os.walk(dir):
        for filename in fnmatch.filter(filenames, pat):
            matches.append(os.path.join(root, filename))
    return matches

def main():
    pat = sys.argv[1]
    dir = os.getcwd()
    files = search(pat, dir)
    for file in files:
        print(file)

if __name__ == "__main__":
    main()