from itertools import chain

def spiral(h, w, s):
    if h == 0:
        return [[]]
    else:
        return [list(range(s, s+w))] + list(zip(*spiral(w, h-1, s+w)[::-1]))

def main():
    for row in spiral(10, 9, 1):
        print(" ".join([f"{num:4d}" for num in row]))

if __name__ == "__main__":
    main()