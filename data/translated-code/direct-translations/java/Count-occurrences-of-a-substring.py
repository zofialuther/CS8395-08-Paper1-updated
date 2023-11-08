def countSubstring(subStr, str):
    count = 0
    loc = str.find(subStr)
    while loc != -1:
        count += 1
        loc = str.find(subStr, loc + len(subStr))
    return count

print(countSubstring("th", "the three truths"))
print(countSubstring("abab", "ababababab"))
print(countSubstring("a*b", "abaabba*bbaba*bbab"))