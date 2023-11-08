needles = ["Washington", "Bush"]
haystack = ["George", "Washington", "was", "the", "first", "president", "George", "Bush", "was", "the", "43rd", "president"]

result = list(map(lambda x: (x, [i for i in range(len(haystack)) if haystack[i] == x]), needles))
print(result)