import sys
from sys import stdin, stdout
from data import isalpha

def split(s):
    return (s[:i], s[i:]) if (i := next((i for i, c in enumerate(s) if not isalpha(c)), len(s))) else (s, "")

def parse(s):
    if not s:
        return ""
    a, w = split(s)
    b, x = w[:1], w[1:]
    c, y = split(x)
    d, z = y[:1], y[1:]
    return a + b + c[::-1] + d + parse(z)

def main():
    stdin.buffer.raw.read(1)
    stdout.buffer.raw.write(parse(sys.stdin.read()).split('.')[0].encode())
    stdout.buffer.raw.write(b'.')

if __name__ == "__main__":
    main()