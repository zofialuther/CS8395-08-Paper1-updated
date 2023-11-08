```python
import sys
from collections import defaultdict
from operator import attrgetter

class Employee:
    def __init__(self, name, id, department, salary):
        self.name = name
        self.id = id
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Department: {self.department}, Salary: {self.salary}"

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    records = defaultdict(list)
    with open("data.txt", "r") as file:
        for line in file:
            rec = line.strip().split(", ")
            employee_list = records[rec[2]]
            if employee_list is None:
                employee_list = []
                records[rec[2]] = employee_list
            employee_list.append(Employee(rec[0], rec[1], rec[2], float(rec[3])))
    for department, employees in records.items():
        print(department)
        employees.sort(key=attrgetter('salary'), reverse=True)
        for employee in employees[:N]:
            print(employee)

if __name__ == "__main__":
    main()
```