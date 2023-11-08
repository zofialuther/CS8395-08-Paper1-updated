def countJewels(stones, jewels):
    jewelset = set(jewels)
    count = 0
    for stone in stones:
        if stone in jewelset:
            count = count + 1
    return count

print(countJewels("aAAbbbb", "aA"))
print(countJewels("ZZ", "z"))