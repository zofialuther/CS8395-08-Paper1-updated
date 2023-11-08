def main():
    y = str(5 ** 4 ** 3 ** 2)
    l = len(y)
    print("5**4**3**2 = " + y[:20] + "..." + y[-20:] + " and has " + str(l) + " digits")

main()