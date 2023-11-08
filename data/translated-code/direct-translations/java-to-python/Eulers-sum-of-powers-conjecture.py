MAX_NUMBER = 250

def main(args):
    found = False
    fifth = [0] * MAX_NUMBER

    for i in range(1, MAX_NUMBER + 1):
        i2 = i * i
        fifth[i - 1] = i2 * i2 * i

    for a in range(MAX_NUMBER):
        for b in range(a, MAX_NUMBER):
            for c in range(b, MAX_NUMBER):
                for d in range(c, MAX_NUMBER):
                    sum = fifth[a] + fifth[b] + fifth[c] + fifth[d]
                    e = fifth.index(sum) if sum in fifth else -1
                    found = (e >= 0)
                    if found:
                        print(f"{a+1}^5 + {b+1}^5 + {c+1}^5 + {d+1}^5 = {e+1}^5")
                        return

main([])