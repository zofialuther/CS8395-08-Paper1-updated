from typing import List, Tuple, Optional

def multisplit(delims: List[str], string: str) -> List[Tuple[str, str, int]]:
    def go(acc: List[str], pos: int, l: List[str]) -> List[Tuple[str, str, int]]:
        if not l:
            return [(acc, '', pos)]
        else:
            s = l[0]
            sx = l[1:]
            result = trysplit(delims, l)
            if result is None:
                return go([s] + acc, pos + 1, sx)
            else:
                d, sxx = result
                return [(acc, d, pos)] + go([], pos + len(d), sxx)

    def trysplit(delims: List[str], s: str) -> Optional[Tuple[str, str]]:
        for d in delims:
            if s.startswith(d):
                return d, s[len(d):]
        return None

    return go([], 0, list(string))

def main():
    parsed = multisplit(["==", "!=", "="], "a!===b=!=c")
    for a, _, _ in parsed:
        print(a)
    print(parsed)

if __name__ == "__main__":
    main()