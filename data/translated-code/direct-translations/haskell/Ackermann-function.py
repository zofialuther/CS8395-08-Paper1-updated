def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

def main():
    for pair in [(0, 0), (3, 4)]:
        print(ack(*pair))

main()