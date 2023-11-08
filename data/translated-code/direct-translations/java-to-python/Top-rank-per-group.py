```python
class Employee:
    def __init__(self, rec):
        self.name = rec[0]
        self.id = rec[1]
        self.salary = int(rec[2])
        self.department = rec[3]

    def __str__(self):
        return f"{self.id} {self.name} {self.salary} {self.department}"

if __name__ == "__main__":
    import sys

    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    records = {}
    with open("data.txt") as file:
        for line in file:
            rec = line.strip().split(", ")
            if rec[3] not in records:
                records[rec[3]] = []
            records[rec[3]].append(Employee(rec))

    for key, val in records.items():
        print(f"\nDepartment {key}")
        for emp in sorted(val, key=lambda x: x.salary, reverse=True)[:N]:
            print(emp)
```