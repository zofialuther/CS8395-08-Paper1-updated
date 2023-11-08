def unsafe(y):
  x = b[y]
  for i in range(1, y + 1):
    t = b[y - i]
    if t == x or t == x - i or t == x + i:
      return True
  return False

def putboard():
  global s
  print("Solution " + str(s))
  for y in range(8):
    for x in range(8):
      if b[y] == x:
        print("|Q", end="")
      else:
        print("|_", end="")
    print("|")

def main():
  global s
  s = 0
  y = 0
  b = [-1] * 8
  while y >= 0:
    b[y] += 1
    while b[y] < 8 and unsafe(y):
      b[y] += 1
    if b[y] < 8:
      if y < 7:
        y += 1
        b[y] = -1
      else:
        putboard()
    else:
      y -= 1