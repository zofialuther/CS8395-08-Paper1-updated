```python
from itertools import permutations

def dinesman():
  permutationsList = list(permutations([1, 2, 3, 4, 5]))
  for permutation in permutationsList:
    baker = permutation[0]
    cooper = permutation[1]
    fletcher = permutation[2]
    miller = permutation[3]
    smith = permutation[4]

    if baker != 5:
      continue
    if cooper != 1:
      continue
    if fletcher == 5 or fletcher == 1:
      continue
    if miller <= cooper:
      continue
    if abs(smith - fletcher) == 1:
      continue
    if abs(fletcher - cooper) == 1:
      continue
    return (baker, cooper, fletcher, miller, smith)

def main():
  solutions = dinesman()
  print(solutions)
```