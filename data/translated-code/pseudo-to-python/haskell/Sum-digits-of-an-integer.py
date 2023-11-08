def digsum(base, n):
    a = 0
    while n != 0:
        q, r = divmod(n, base)
        a = a + r
        n = q
    return a

def main():
    result = digsum(16, 255)
    print(result)

main()