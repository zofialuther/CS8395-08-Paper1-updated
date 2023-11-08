from java.lang import System
from java.util import Arrays, Comparator

class ParallelCalculations:
    NUMBERS = [
      12757923,
      12878611,
      12878893,
      12757923,
      15808973,
      15780709,
      197622519
    ]

    @staticmethod
    def main(*arguments):
      stream(Arrays.stream(NUMBERS))
        .unordered()
        .parallel()
        .mapToObj(ParallelCalculations.minimalPrimeFactor)
        .max(Comparator.comparing(lambda a: a[0]))
        .ifPresent(lambda res: System.out.printf(
          "%d has the largest minimum prime factor: %d%n",
          res[1],
          res[0]
        ))

    @staticmethod
    def minimalPrimeFactor(n):
      i = 2
      while n >= i * i:
        if n % i == 0:
          return [i, n]
        i += 1
      return [n, n]