def weave(strings):
    thread = zipWith((lambda x, y: x + y), strings, strings[::-1])
    return [''.join([c if c != '█' else ' ' for c in s]) for s in thread]

def carpet(n):
    return '\n'.join(iterate(weave, ["██"])[n])

def main():
    for i in range(3):
        print(carpet(i))

main()