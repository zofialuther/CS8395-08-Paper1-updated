i = 1
while i <= 10:
    if i % 5 == 0:
        print(i)
        i += 1
        continue
    else:
        print(i, end=", ")
        i += 1