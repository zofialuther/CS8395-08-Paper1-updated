```python
class OIDListSorting:
    def main(self, args):
        dot = "\\."
        oids_comparator = lambda o1, o2: 
            o1Numbers = o1.split(dot)
            o2Numbers = o2.split(dot)
            for i in range(len(o1Numbers)):
                if i == len(o1Numbers) and i == len(o2Numbers):
                    return 0
                if i == len(o1Numbers):
                    return -1
                if i == len(o2Numbers):
                    return 1
                nextO1Number = int(o1Numbers[i])
                nextO2Number = int(o2Numbers[i])
                result = nextO1Number - nextO2Number
                if result != 0:
                    return result

        oids = ["1.3.6.1.4.1.11.2.17.19.3.4.0.10", "1.3.6.1.4.1.11.2.17.5.2.0.79", "1.3.6.1.4.1.11.2.17.19.3.4.0.4",
                  "1.3.6.1.4.1.11150.3.4.0.1", "1.3.6.1.4.1.11.2.17.19.3.4.0.1", "1.3.6.1.4.1.11150.3.4.0"]
        oids.sort(key=oids_comparator)
        for oid in oids:
            print(oid)
```