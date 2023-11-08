def out(x):
    if x % 5 == 0:
        print(x)
    else:
        print(str(x) + ", ")

for i in range(1, 11):
    out(i)