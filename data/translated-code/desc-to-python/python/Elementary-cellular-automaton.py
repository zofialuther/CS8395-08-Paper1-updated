def eca(rule, initial, steps):
    ca_rule = format(rule, '08b')
    current = initial
    for _ in range(steps):
        print(''.join('X' if x else ' ' for x in current))
        current = [int(ca_rule[7 - (4*current[i-1] + 2*current[i] + current[(i+1)%len(current)])]) for i in range(len(current))]

def main():
    eca(30, [0]*100 + [1] + [0]*100, 50)
    eca(90, [0]*100 + [1] + [0]*100, 50)
    eca(182, [0]*100 + [1] + [0]*100, 50)

main()