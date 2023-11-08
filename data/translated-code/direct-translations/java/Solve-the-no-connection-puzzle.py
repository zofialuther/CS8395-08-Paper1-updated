from random import shuffle

links = [
    [2, 3, 4],  # A to C,D,E
    [3, 4, 5],  # B to D,E,F
    [2, 4],     # D to C, E
    [5],        # E to F
    [2, 3, 4],  # G to C,D,E
    [3, 4, 5]   # H to D,E,F
]

pegs = [0] * 8

def main():
    vals = list(range(1, 9))
    while not solved():
        shuffle(vals)
        for i in range(8):
            pegs[i] = vals[i]
    print_result()

def solved():
    for i in range(len(links)):
        for peg in links[i]:
            if abs(pegs[i] - peg) == 1:
                return False
    return True

def print_result():
    print(f"  {pegs[0]} {pegs[1]}")
    print(f"{pegs[2]} {pegs[3]} {pegs[4]} {pegs[5]}")
    print(f"  {pegs[6]} {pegs[7]}")

if __name__ == "__main__":
    main()