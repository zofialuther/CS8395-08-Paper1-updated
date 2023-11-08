from collections import namedtuple
from itertools import groupby

# Define the employee record namedtuple
Employee = namedtuple('Employee', ['name', 'department', 'salary'])

# Sample database of employee records
employees = [
    Employee('Alice', 'HR', 60000),
    Employee('Bob', 'IT', 80000),
    Employee('Charlie', 'HR', 75000),
    Employee('David', 'IT', 70000),
    Employee('Eve', 'Finance', 90000),
    Employee('Frank', 'Finance', 95000)
]

# Sort the employee records by department and salary
employees.sort(key=lambda emp: (emp.department, emp.salary), reverse=True)

# Define the top N earners to display
top_n_earners = 2

# Group the sorted employee records by department
for department, group in groupby(employees, key=lambda emp: emp.department):
    print(f"Top {top_n_earners} earners in {department}:")
    for emp in list(group)[:top_n_earners]:
        print(f"{emp.name}: {emp.salary}")