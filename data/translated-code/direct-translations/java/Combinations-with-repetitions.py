```python
import itertools

class MultiCombinations:

    def __init__(self, objects, k):
        k = max(0, k)
        my_objects = [obj for obj in objects for _ in range(k)]
        self.comb = itertools.combinations(my_objects, k)
        self.set = set()
        self.next_elem = None

    def has_more_elements(self):
        ret = False
        self.next_elem = None
        old_count = len(self.set)
        try:
            while True:
                elem = next(self.comb)
                str_elem = "".join(["%" + str(e) + "~" for e in elem])
                self.set.add(str_elem)
                if len(self.set) > old_count:
                    self.next_elem = elem
                    ret = True
                    break
        except StopIteration:
            pass
        return ret

    def next_element(self):
        return self.next_elem

    @staticmethod
    def c(n, k):
        return math.comb(n + k - 1, k)
```