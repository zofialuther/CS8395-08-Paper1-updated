def vdc(n):
    vdc = 0
    denom = 1
    while n != 0:
        vdc += n % 2.0 / (denom * 2)
        n //= 2
        denom *= 2
    return vdc

def main():
    for i in range(11):
        print(vdc(i))

if __name__ == "__main__":
    main()