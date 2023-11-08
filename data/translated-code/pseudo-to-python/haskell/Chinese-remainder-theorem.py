def egcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        s, t = egcd(b, a % b)
        q, r = divmod(a, b)
        return (t, s - q * t)

def modInv(a, b):
    x, y = egcd(a, b)
    if a * x + b * y == 1:
        return x
    else:
        return "No modular inverse for " + str(a) + " and " + str(b)

def chineseRemainder(residues, modulii):
    modPI = 1
    for m in modulii:
        modPI *= m
    crtModulii = [modPI // m for m in modulii]
    result = [modInv(crtModulii[i], modulii[i]) for i in range(len(modulii))]
    total = sum(crtModulii[i] * residues[i] * result[i] for i in range(len(residues)))
    return total % modPI

def main():
    for pair in [([10, 4, 12], [11, 12, 13]), ([10, 4, 9], [11, 22, 19]), ([2, 3, 2], [3, 5, 7])]:
        result = chineseRemainder(pair[0], pair[1])
        print(result)

main()