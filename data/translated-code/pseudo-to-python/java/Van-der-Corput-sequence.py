def vdc(n):
    vdc = 0
    denom = 1
    while n != 0:
        vdc = vdc + n % 2.0 / (denom * 2)
        n = n / 2
    return vdc

def main(args):
    for i in range(11):
        print(vdc(i))