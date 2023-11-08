from cmath import rect, pi

def roots_of_unity(n):
    return [rect(1, 2 * pi * k / n) for k in range(n)]

def main():
    for root in roots_of_unity(3):
        print(root)

if __name__ == "__main__":
    main()