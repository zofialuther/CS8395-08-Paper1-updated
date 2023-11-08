cof = [
  76.18009172947146,
  -86.50532032941677,
  24.01409824083091,
  -1.231739572450155,
  0.001208650973866179,
  -0.000005395239384953
]

ser = 1.000000000190015

def gammaln(xx):
  tmp_ = (xx + 5.5) - (xx + 0.5) * log(xx + 5.5)
  ser_ = ser + sum([a / (xx + 1 + i) for i, a in enumerate(cof)])
  return -tmp_ + log(2.5066282746310005 * ser_ / xx)

for i in range(1, 11):
  print(gammaln(i / 10))