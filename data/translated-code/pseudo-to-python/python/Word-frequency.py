import collections
import re
import string
import sys

def main():
    with open(sys.argv[1], 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        counter = collections.Counter(words)
        for word, count in counter.most_common(int(sys.argv[2])):
            print(word, count)

if __name__ == "__main__":
    main()