def jewelCount(jewels, s):
    count = 0
    for i in range(len(s)):
        if s[i] in jewels:
            count += 1
    return count

print(jewelCount("aA", "aAAbbbb"))
print(jewelCount("z", "ZZ"))