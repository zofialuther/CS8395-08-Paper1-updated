def countJewels(stones, jewels):
    jewel_set = set(jewels)
    count = sum(1 for stone in stones if stone in jewel_set)
    return count

test_case_1 = countJewels("aAAbbbb", "aA")
test_case_2 = countJewels("ZZ", "z")
print(test_case_1)
print(test_case_2)