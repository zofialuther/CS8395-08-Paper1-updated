print(*((lambda x=x: ''.join(chr(c) for c in (102, 105)) + (2 * chr(122)) + ''.join(chr(c) for c in (98, 117)) + (2 * chr(122)) + '\n' if x % (30 >> 1) == 0 else ''.join(chr(c) for c in (102, 105)) + (2 * chr(122)) + '\n' if x % (6 >> 1) == 0 else ''.join(chr(c) for c in (98, 117)) + (2 * chr(122)) + '\n' if x % (10 >> 1) == 0 else str(x) + '\n')() for x in range(1, 101)))
