def ordinalAbbrev(n):
    ans = "th"
    if n % 100 / 10 == 1:
        return ans
    else:
        if n % 10 == 1:
            ans = "st"
        elif n % 10 == 2:
            ans = "nd"
        elif n % 10 == 3:
            ans = "rd"
    return ans

def main():
    for i in range(26):
        print(str(i) + ordinalAbbrev(i) + " ", end="")
    print("\n")
    for i in range(250, 266):
        print(str(i) + ordinalAbbrev(i) + " ", end="")
    print("\n")
    for i in range(1000, 1026):
        print(str(i) + ordinalAbbrev(i) + " ", end="")