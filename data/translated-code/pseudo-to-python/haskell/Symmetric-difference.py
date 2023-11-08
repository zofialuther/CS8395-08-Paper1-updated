a = ["Serena", "Jim", "Tom"]
b = ["Jim", "Tom", "Kate"]

resultA = list(set(b) - set(a))
resultB = list(set(a) - set(b))

print(resultA)
print(resultB)