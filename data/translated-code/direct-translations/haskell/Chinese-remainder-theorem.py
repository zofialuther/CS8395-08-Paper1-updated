from typing import List, Tuple, Union

def egcd(a: int, b: int) -> Tuple[int, int]:
    if b == 0:
        return (1, 0)
    else:
        s, t = egcd(b, a % b)
        q, r = divmod(a, b)
        return (t, s - q * t)

def modInv(a: int, b: int) -> Union[str, int]:
    x, y = egcd(a, b)
    if a * x + b * y == 1:
        return x
    else:
        return "No modular inverse for " + str(a) + " and " + str(b)

def chineseRemainder(residues: List[int], modulii: List[int]) -> Union[str, int]:
    crtModulii = [product(modulii) // m for m in modulii]
    invs = [modInv(crt, m) for crt, m in zip(crtModulii, modulii)]
    if all(isinstance(inv, int) for inv in invs):
        result = sum(r * crt * inv for r, crt, inv in zip(residues, crtModulii, invs))
        return result % product(modulii)
    else:
        return "No modular inverse for provided residues and modulii"

def main():
    problems = [([10, 4, 12], [11, 12, 13]), ([10, 4, 9], [11, 22, 19]), ([2, 3, 2], [3, 5, 7])]
    for residues, modulii in problems:
        result = chineseRemainder(residues, modulii)
        if isinstance(result, int):
            print(result)
        else:
            print(result)

if __name__ == "__main__":
    main()