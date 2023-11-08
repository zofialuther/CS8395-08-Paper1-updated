from fractions import Fraction
import itertools

# The Continued Fraction
def CF(a, b, t):
  terms = list(itertools.islice(zip(a, b), t))
  z = Fraction(1,1)
  for a, b in reversed(terms):
    z = a + b / z
  return z

# Approximates a fraction to a string
def pRes(x, d):
  q, x = divmod(x, 1)
  res = str(q)
  res += "."
  for i in range(d):
    x *= 10
    q, x = divmod(x, 1)
    res += str(q)
  return res

# Test the Continued Fraction for sqrt2
def sqrt2_a():
  yield 1
  while True:
    yield 2

def sqrt2_b():
  while True:
    yield 1

cf = CF(sqrt2_a(), sqrt2_b(), 950)
print(pRes(cf, 200))

# Test the Continued Fraction for Napier's Constant
def Napier_a():
  yield 2
  for x in itertools.count(1):
    yield x

def Napier_b():
  yield 1
  for x in itertools.count(1):
    yield x

cf = CF(Napier_a(), Napier_b(), 950)
print(pRes(cf, 200))

# Test the Continued Fraction for Pi
def Pi_a():
  yield 3
  while True:
    yield 6

def Pi_b():
  for x in itertools.count(1, 2):
    yield x*x

cf = CF(Pi_a(), Pi_b(), 950)
print(pRes(cf, 10))