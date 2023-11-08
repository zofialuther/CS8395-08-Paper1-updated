def traverse(f, arr):
  result = []
  for i in range(len(arr)):
    result.append(f(arr[i]))
  return result

def tf(arr):
  return traverse(lambda x: [1, 0], arr)

def wrongness(ns, ps):
  result = []
  for i in range(len(ns)):
    if ns[i] != ps[i](ns):
      result.append(i)
  return result

def statements(n):
  result = []
  if n == 12:
    result.append(lambda arr: len(arr) == 12)
  if 3 < len(statements) - 6:
    result.append(lambda arr: arr[3] < len(arr) - 6)
  # ... continue with the rest of the statements in a similar manner

def testall(s, n):
  result = []
  for i in range(len(s)):
    for j in range(len(tf(s))):
      b = tf(s)[j]
      w = wrongness(b, s)
      if len(w) == n:
        result.append([b, w])
  return result

def main():
  t = testall(statements, 0)
  print("Answer")
  for item in t:
    print(item)
  print("Near misses")
  t1 = testall(statements, 1)
  for item in t1:
    print(item)