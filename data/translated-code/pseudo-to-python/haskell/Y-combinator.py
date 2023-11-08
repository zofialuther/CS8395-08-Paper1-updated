def fix(f):
  return f(fix(f))

def fac(n):
  def helper(f, n, i):
    if i <= 0:
      return n
    else:
      return f(i * n, i - 1)
  return fix(helper, 1)

def fib(n):
  def helper(fnc, f, s, i):
    if i <= 1:
      return f
    else:
      return (f + s, lambda n: n if fnc(s, n, i - 1) else None)
  return fix(helper, 0, 1)

def fibs():
  def helper(fnc, f, s):
    return [0, 1, fix(zipP(f, fnc, s, tail(s)))]
  return fix(helper, 0, 1)

def main():
  mapM_(
    lambda result: print(result),
    [map(fac, [1, 20]), map(fib, [1, 20]), take(20, fibs())]
  )