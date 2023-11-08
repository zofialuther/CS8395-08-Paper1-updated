def show_ascii_table():
    for i in range(32, 128):
        if i == 32 or i == 127:
            s = "Spc" if i == 32 else "Del"
            print(f"{i}: {s} ", end="")
        else:
            print(f"{i}: {chr(i)}   ", end="")
        if (i-1) % 6 == 0:
            print()

show_ascii_table()