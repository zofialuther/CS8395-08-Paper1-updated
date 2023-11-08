# Python code
def countJewels(stones, jewels):
    bag = set(jewels)
    count = 0
    for c in stones:
        if c in bag:
            count += 1
    return count

print(countJewels("aAAbbbb", "aA"))
print(countJewels("ZZ", "z"))