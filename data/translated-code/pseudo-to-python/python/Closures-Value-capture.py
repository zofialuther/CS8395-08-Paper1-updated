funcs = []

for i in range(10):
    funcs.append(lambda i=i: lambda: i * i)

print(funcs[3]())