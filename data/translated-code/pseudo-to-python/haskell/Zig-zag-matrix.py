def show2d(a):
  l, h = len(a[0]), len(a)
  for y in range(h):
    for x in range(l):
      print(f"{a[y][x]}", end=" ")
    print()
    
def main():
  for pair in [(3, 3), (4, 4), (10, 2)]:
    show2d(pair)

main()