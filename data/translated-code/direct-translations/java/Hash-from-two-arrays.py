from collections import defaultdict

def main(args):
    keys = ["a", "b", "c"]
    vals = [1, 2, 3]
    hash_map = defaultdict(int)

    for i in range(len(keys)):
        hash_map[keys[i]] = vals[i]

if __name__ == "__main__":
    main([])