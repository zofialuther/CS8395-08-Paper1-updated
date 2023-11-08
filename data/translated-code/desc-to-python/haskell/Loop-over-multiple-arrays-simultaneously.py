from itertools import product
from sequence import sequence, parallelListComp

def main():
    strings = ["abc", "ABC", "123"]
    combinations = parallelListComp([list(s) for s in strings])
    sequence(print, combinations)

if __name__ == "__main__":
    main()