```python
# Python code
import sys

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

employee_records = [
    Employee('John', 'HR', 50000),
    Employee('Jane', 'HR', 55000),
    Employee('Mike', 'IT', 60000),
    Employee('Sara', 'IT', 65000)
]

top_earners_to_display = int(sys.argv[1]) if len(sys.argv) > 1 else 3

employee_map = {}
for employee in employee_records:
    if employee.department in employee_map:
        employee_map[employee.department].append(employee)
    else:
        employee_map[employee.department] = [employee]

for department, employees in employee_map.items():
    employees.sort(key=lambda x: x.salary, reverse=True)
    print(f"Top {top_earners_to_display} earners in {department} department:")
    for i in range(min(top_earners_to_display, len(employees))):
        print(f"{employees[i].name} - {employees[i].salary}")
```