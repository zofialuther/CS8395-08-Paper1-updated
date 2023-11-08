def main():
    fourSquare(1, 7, True, True)
    fourSquare(3, 9, True, True)
    fourSquare(0, 9, False, False)

def fourSquare(low, high, unique, print_output):
    count = 0

    if print_output:
        print("a b c d e f g")

    for a in range(low, high+1):
        for b in range(low, high+1):
            if notValid(unique, a, b):
                continue
            fp = a + b
            for c in range(low, high+1):
                if notValid(unique, c, a, b):
                    continue
                for d in range(low, high+1):
                    if notValid(unique, d, a, b, c):
                        continue
                    if fp != b + c + d:
                        continue
                    for e in range(low, high+1):
                        if notValid(unique, e, a, b, c, d):
                            continue
                        for f in range(low, high+1):
                            if notValid(unique, f, a, b, c, d, e):
                                continue
                            if fp != d + e + f:
                                continue
                            for g in range(low, high+1):
                                if notValid(unique, g, a, b, c, d, e, f):
                                    continue
                                if fp != f + g:
                                    continue
                                count += 1
                                if print_output:
                                    print(a, b, c, d, e, f, g)

    if unique:
        print("There are " + str(count) + " unique solutions in [" + str(low) + ", " + str(high) + "]")
    else:
        print("There are " + str(count) + " non-unique solutions in [" + str(low) + ", " + str(high) + "]")

def notValid(unique, needle, haystack):
    for p in haystack:
        if p == needle:
            return True
    return False