def o(O):
  list = [0, 1, 2, 3, 4, 5, 6, 7]
  if O in list:
    return True
  else:
    return False

def octal(O):
  return o(O)

def octal(A, B):
  O = octal(A)
  T = octal(B)
  newList = O + [T]
  if A != 0:
    return newList

def octalize(X):
  X = octal(X)
  for i in range(len(X)):
    print(X[i])