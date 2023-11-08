def dragon(n):
    if n == 0:
        return 'FX+'
    else:
        return dragon(n-1).replace('X', '+YF').replace('Y', 'FX-')

def main():
    print(dragon(14))

main()