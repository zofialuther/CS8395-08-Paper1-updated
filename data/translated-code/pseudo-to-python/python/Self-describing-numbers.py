def isSelfDescribing(n):
    s = str(n)
    for i in range(len(s)):
        if s.count(str(i)) != int(s[i]):
            return False
    return True

result_list = []
for x in range(4000000):
    if isSelfDescribing(x):
        result_list.append(x)

print(result_list)

test_values = (1210, 2020, 21200, 3211000, 42101000, 521001000, 6210001000)
for value in test_values:
    print(value, isSelfDescribing(value))