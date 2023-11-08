string1 = 'abc'
string2 = 'ABC'
string3 = '123'

combined = list(zip(string1, string2, string3))
result = list(map(lambda x: ''.join(x), combined))

for item in result:
    print(item)