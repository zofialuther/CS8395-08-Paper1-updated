x = 0
while x < 30000:
    if pow(x, 2, 1000000) == 269696:
        print(x)
        break
    x += 1