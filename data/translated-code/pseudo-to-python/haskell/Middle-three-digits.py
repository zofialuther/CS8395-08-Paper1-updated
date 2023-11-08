def mid3(n):
  if n < 100:
    return "too small"
  elif len(str(n)) % 2 == 0:
    return "even number of digits"
  else:
    s = str(n)
    lng = len(s)
    return s[(lng - 3) // 2 : (lng - 3) // 2 + 3]

def main():
  xs = [ 123, 12345, 1234567, 987654321, 10001, -10001, -123, -100, 100, -12345, 1, 2, -1, -10, 2002, -2002, 0 ]
  w = max(len(str(x)) for x in xs)
  for n in xs:
    print(justifyRight(w, ' ', str(n)) + " -> " + mid3(n))

def justifyRight(n, c, s):
  return (n - len(s)) * c + s

main()