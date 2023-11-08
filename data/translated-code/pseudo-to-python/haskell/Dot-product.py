def dotp(a, b):
    if len(a) == len(b):
        return sum([a[i] * b[i] for i in range(len(a))])
    else:
        print("Vector sizes must match")

def main():
    print(dotp([1, 3, -5], [4, -2, -1]))

main()