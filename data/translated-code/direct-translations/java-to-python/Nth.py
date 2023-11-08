def ordinalAbbrev(n):
    ans = "th" # most of the time it should be "th"
    if n % 100 // 10 == 1:
        return ans # teens are all "th"
    if n % 10 == 1:
        ans = "st"
    elif n % 10 == 2:
        ans = "nd"
    elif n % 10 == 3:
        ans = "rd"
    return ans

def main():
    for i in range(26):
        print(i, ordinalAbbrev(i), end=" ")
    print()
    for i in range(250, 266):
        print(i, ordinalAbbrev(i), end=" ")
    print()
    for i in range(1000, 1026):
        print(i, ordinalAbbrev(i), end=" ")

main()