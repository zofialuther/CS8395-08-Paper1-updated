def jewelCount(jewels, s):
    def go(c, count):
        if c in jewels:
            return count + 1
        else:
            return count
    return len([go(c, 0) for c in s])

# Test
print(jewelCount("aA", "aAAbbbb"))
print(jewelCount("z", "ZZ"))