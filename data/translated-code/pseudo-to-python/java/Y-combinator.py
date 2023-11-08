def Y(f):
  r = lambda w: f(lambda x: w(w)(x))
  return r(r)

def fib(n):
  return Y(lambda f: lambda n: 1 if n <= 2 else f(n - 1) + f(n - 2))(n)

def fac(n):
  return Y(lambda f: lambda n: 1 if n <= 1 else n * f(n - 1))(n)

print("fib(10) = " + str(fib(10)))
print("fac(10) = " + str(fac(10)) )