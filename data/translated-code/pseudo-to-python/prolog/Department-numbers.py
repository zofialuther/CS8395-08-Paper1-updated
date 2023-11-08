def dept(X):
  return X >= 1 and X <= 7

def police(X):
  return X in [2, 4, 6]

def fire(X):
  return dept(X)

def san(X):
  return dept(X)

def assign(A, B, C):
  if police(A) and fire(B) and san(C) and A != B and A != C and B != C and 12 == A + B + C:
    return [A, B, C]

def main():
  print("P F S\n")
  for i in range(1, 8):
    for j in range(1, 8):
      for k in range(1, 8):
        result = assign(i, j, k)
        if result:
          print(f"{result[0]} {result[1]} {result[2]}\n")
          
main()