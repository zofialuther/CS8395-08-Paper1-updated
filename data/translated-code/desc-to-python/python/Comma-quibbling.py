def commaQuibble(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return " and ".join(lst)
    else:
        return ", ".join(lst[:-1]) + ", and " + lst[-1]

# Test cases
test1 = ["apple", "banana", "cherry"]
print(test1, "->", commaQuibble(test1))

test2 = ["one"]
print(test2, "->", commaQuibble(test2))

test3 = ["hello", "world"]
print(test3, "->", commaQuibble(test3))