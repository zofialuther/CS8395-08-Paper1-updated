from itertools import chain

uppersAndLowers = (
    list(filter(isUpper, map(chr, range(1, 0x10ffff)))),
    list(filter(isLower, map(chr, range(1, 0x10ffff)))
)

def main():
    upper, lower = uppersAndLowers
    print("Upper:")
    for chunk in chunksOf(70, upper):
        print("".join(chunk))
    print("\nLower:")
    for chunk in chunksOf(70, lower):
        print("".join(chunk))

if __name__ == "__main__":
    main()