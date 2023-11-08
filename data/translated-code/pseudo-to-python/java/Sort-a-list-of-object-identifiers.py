```python
import re

class OIDListSorting:
    def main(self, arr):
        dot = "\\."
        
        def oids_comparator(o1, o2):
            o1Numbers = re.split(dot, o1)
            o2Numbers = re.split(dot, o2)
            
            for i in range(max(len(o1Numbers), len(o2Numbers))):
                if i == len(o1Numbers) == len(o2Numbers):
                    return 0
                elif i == len(o1Numbers):
                    return -1
                elif i == len(o2Numbers):
                    return 1
                nextO1Number = int(o1Numbers[i])
                nextO2Number = int(o2Numbers[i])
                result = nextO1Number - nextO2Number
                if result != 0:
                    return result
            return 0
        
        oids = ["1.3.6.1.4.1.37523.8.1.1.1", "1.3.6.1.4.1.37523.8.1.10.1", "1.3.6.1.4.1.37523.8.1.3.1"]
        oids.sort(key=oids_comparator)
        for oid in oids:
            print(oid)

oidListSorting = OIDListSorting()
oidListSorting.main([])
```