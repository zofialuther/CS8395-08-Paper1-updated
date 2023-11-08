from dataclasses import dataclass
from operator import itemgetter
from itertools import groupby

@dataclass
class Employee:
    nr: int
    dep: str
    name: str
    sal: float

employees = [
    (1001, "AB", "Janssen A.H.", 41000),
    (101, "KA", "'t Woud B.", 45000),
    # ... (rest of the employees)
]

def first_n(n, o1, o2, x):
    sorted_x = sorted(x, key=itemgetter(o1))
    grouped_x = [list(group) for _, group in groupby(sorted_x, key=itemgetter(o1))]
    sorted_grouped_x = [sorted(group, key=itemgetter(o2), reverse=True)[:n] for group in grouped_x]
    return sorted_grouped_x

def main():
    print("%-16s %3s %10s" % ("NAME", "DEP", "TIP"))
    print("=" * 31)
    for group in first_n(3, itemgetter(1), itemgetter(3), employees):
        for employee in group:
            print("%-16s %3s %10.2f" % (employee.name, employee.dep, employee.sal))

if __name__ == "__main__":
    main()