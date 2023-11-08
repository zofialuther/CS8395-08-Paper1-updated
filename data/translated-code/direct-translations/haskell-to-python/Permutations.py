from itertools import permutations

def ins(x, xs, n):
    return xs[:n] + [x] + xs[n:]

def all_permutations(lst):
    return list(permutations(lst))

def main():
    print(all_permutations([1, 2, 3]))

if __name__ == "__main__":
    main()