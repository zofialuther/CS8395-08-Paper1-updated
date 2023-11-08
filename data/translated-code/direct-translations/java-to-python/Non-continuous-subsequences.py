def seqR(s, c, i, added):
    if i == len(s):
        if len(c.strip()) > added:
            print(c)
    else:
        seqR(s, c + s[i], i + 1, added + 1)
        seqR(s, c + ' ', i + 1, added)

def main():
    seqR("1234", "", 0, 0)

if __name__ == "__main__":
    main()