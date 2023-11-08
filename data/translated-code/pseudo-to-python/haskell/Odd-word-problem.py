```python
import string

def split(s):
  return ''.join(filter(str.isalpha, s))

def parse(s):
  if not s:
    return ''
  else:
    a, w = split(s)
    b, x = w[:1], w[1:]
    c, y = split(x)
    d, z = y[:1], y[1:]
    return a + b + c[::-1] + d + parse(z)

def main():
  import sys
  sys.stdin = open(0)
  sys.stdout = open(1)
  content = sys.stdin.read()
  result = parse(content).split('.')[0]
  print(result)
  print(".")

if __name__ == "__main__":
  main()
```