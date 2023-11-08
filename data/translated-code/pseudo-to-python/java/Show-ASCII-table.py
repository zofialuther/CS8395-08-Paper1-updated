i = 0
for i in range(32, 128):
    if i == 32 or i == 127:
        s = ""
        if i == 32:
            s = "Spc"
        else:
            s = "Del"
        print(i, s)
    else:
        print(i, chr(i))
    if (i-31) % 6 == 0:
        print("\n")