```python
def isBrilliant(n):
  primeFactors = find_prime_factors(n)
  if len(primeFactors) == 2:
    if len(str(primeFactors[0])) == len(str(primeFactors[1])):
      return True
    else:
      return False
  else:
    return False

def main():
  indexedBrilliants = [(i, n) for i, n in enumerate(range(1, 101)) if isBrilliant(n)]
  print_table_of_chunks(indexedBrilliants, 10)
  print("(index, brilliant)")
  compare_length_of_brilliant_numbers(indexedBrilliants)

def table(gap, rows):
  ws = [max(len(str(e)) for e in col) for col in zip(*rows)]
  pw = lambda i, e: str(e).rjust(ws[i])
  for r in rows:
    print(' '.join(pw(i, e) for i, e in enumerate(r)))

```