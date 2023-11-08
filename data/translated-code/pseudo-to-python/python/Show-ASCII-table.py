def asciiName(n):
    if 32 > n or 127 < n:
        return ''
    elif 32 == n:
        return 'Spc'
    elif 127 == n:
        return 'Del'
    else:
        return chr(n)

def asciiEntry(n):
    k = asciiName(n)
    if '' == k:
        return k
    else:
        return str(n).rjust(3, ' ') + ' : ' + k

def chunksOf(n):
    def chunks(xs):
        result = []
        for i in range(0, len(xs), n):
            result.append(xs[i:i + n])
        return result
    return chunks

def asciiTable():
    return unlines(
        ''.join(c.ljust(12, ' ') for c in xs) for xs in zip(*chunksOf(16)([asciiEntry(n) for n in range(32, 128)])
    )

def unlines(xs):
    return '\n'.join(xs)

def main():
    print(asciiTable())

if __name__ == "__main__":
    main()