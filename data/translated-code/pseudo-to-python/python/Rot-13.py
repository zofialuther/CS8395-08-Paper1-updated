lets = "abcdefghijklmnopqrstuvwxyz"
key = {}
for i in range(26):
    key[lets[i]] = lets[(i + 13) % 26]
for i in range(26):
    key[lets[i].upper()] = key[lets[i]].upper()

def encode(x):
    result = ""
    for c in x:
        result += key.get(c, c)
    return result

if __name__ == '__main__':
    print("Peform line-by-line rot-13 encoding on any files listed on our command line or act as a standard UNIX filter (if no arguments specified).")
    import fileinput
    for line in fileinput.input():
        print(encode(line))