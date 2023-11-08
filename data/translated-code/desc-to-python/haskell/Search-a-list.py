needles = ["Washington", "Bush"]
haystack = ["George", "Washington", "John", "Adams", "George", "Bush", "Thomas", "Jefferson"]

result = list(map(lambda x: (x, [i for i, y in enumerate(haystack) if y == x]), needles))
print(result)