```python
import com.objectwave.utility.*
import java.util.*

class MultiCombinations:
    
    def __init__(self, objects, k):
        k = max(0, k)
        my_objects = [None] * len(objects) * k
        for i in range(len(objects)):
            for j in range(k):
                my_objects[i * k + j] = objects[i]
        self.comb = Combinations(my_objects, k)
        self.set = set()
        self.next_elem = None
    
    def hasMoreElements(self):
        ret = False
        self.next_elem = None
        old_count = len(self.set)
        while self.comb.hasMoreElements():
            elem = self.comb.nextElement()
            str = ""
            for i in range(len(elem)):
                str += "%" + str(elem[i]) + "~"
            self.set.add(str)
            if len(self.set) > old_count:
                self.next_elem = elem
                ret = True
                break
        return ret
    
    def nextElement(self):
        return self.next_elem
    
    @staticmethod
    def c(n, k):
        return Combinatoric.c(n + k - 1, k)
```