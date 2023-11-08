```python
from functools import cmp_to_key
from operator import itemgetter
from itertools import groupby

class Employee:
    def __init__(self, nr, dep, name, sal):
        self.nr = nr
        self.dep = dep
        self.name = name
        self.sal = sal

employees = [
    Employee(1001, "AB", "Janssen A.H.", 41000),
    Employee(101, "KA", "'t Woud B.", 45000),
    ...
]

def first_n(n, o1, o2, x):
    sorted_x = sorted(x, key=itemgetter(o1))
    grouped_x = [list(group) for key, group in groupby(sorted_x, key=itemgetter(o1))]
    return [sorted(sublist, key=itemgetter(o2), reverse=True)[:n] for sublist in grouped_x]

def main():
    print("%-16s %3s %10s" % ("NAME", "DEP", "SALARY"))
    print("="*31)
    for sublist in first_n(3, "dep", "sal", employees):
        for emp in sublist:
            print("%-16s %3s %10.2g" % (emp.name, emp.dep, emp.sal))

main()
```