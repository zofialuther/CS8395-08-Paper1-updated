```python
from functools import cmp_to_key

class IntConcat:
    @staticmethod
    def compare(a, b):
        if str(a) + str(b) < str(b) + str(a):
            return -1
        else:
            return 1

integers1 = [3, 30, 34, 5, 9]
integers2 = [2, 4, 6, 8, 10]

sorted_integers1 = sorted(integers1, key=cmp_to_key(IntConcat.compare))
sorted_integers2 = sorted(integers2, key=cmp_to_key(IntConcat.compare))

concatenated_result = ''.join(map(str, sorted_integers1)) + ''.join(map(str, sorted_integers2))
print(concatenated_result)
```