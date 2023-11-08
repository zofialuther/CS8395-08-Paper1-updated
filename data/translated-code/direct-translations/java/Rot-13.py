```python
import sys

def main():
    if len(sys.argv) >= 2:
        for file in sys.argv[1:]:
            with open(file, 'rb') as f:
                rot13(f, sys.stdout.buffer)
    else:
        rot13(sys.stdin.buffer, sys.stdout.buffer)

def rot13(in_stream, out_stream):
    while True:
        ch = in_stream.read(1)
        if not ch:
            break
        out_stream.write(rot13_char(ch[0]))

def rot13_char(ch):
    if b'A' <= ch <= b'Z':
        return bytes([((ch - ord(b'A')) + 13) % 26 + ord(b'A')])
    if b'a' <= ch <= b'z':
        return bytes([((ch - ord(b'a')) + 13) % 26 + ord(b'a')])
    return bytes([ch])

if __name__ == "__main__":
    main()
```