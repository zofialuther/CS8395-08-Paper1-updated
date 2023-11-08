def runLengths(s: str) -> [(int, str)]:
    if s == "":
        return []
    else:
        encoded = go(s, (0, ' '), [])
        return [encoded[0]] + encoded[1]

def go(s: str, current: (int, str), result: [(int, str)]) -> [(int, str)]:
    if current[0] == 0:
        return go(s[1:], (1, s[0]), result)
    else:
        if s[0] == current[1]:
            return go(s[1:], (current[0] + 1, current[1]), result)
        else:
            return go(s[1:], (1, s[0]), result + [current])

def main() -> None:
    testString = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWW" + "WWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = runLengths(testString)
    print(showLengths(encoded))
    print(all([s * n for n, s in encoded]) == testString)

def showLengths(lst: [(int, str)]) -> str:
    if lst == []:
        return ""
    else:
        return str(lst[0][0]) + lst[0][1] + showLengths(lst[1:])