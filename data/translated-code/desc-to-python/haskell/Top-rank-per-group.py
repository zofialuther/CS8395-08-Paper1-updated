```python
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

employees = [Employee("John", "HR", 50000),
             Employee("Alice", "IT", 60000),
             Employee("Bob", "HR", 55000),
             Employee("Eve", "IT", 62000),
             Employee("Mike", "Finance", 70000)]

def sort_employees_by_salary(employees):
    return sorted(employees, key=lambda x: x.salary, reverse=True)

def group_employees_by_department(employees):
    groups = {}
    for employee in employees:
        if employee.department in groups:
            groups[employee.department].append(employee)
        else:
            groups[employee.department] = [employee]
    return groups

def main():
    sorted_employees = sort_employees_by_salary(employees)
    grouped_employees = group_employees_by_department(sorted_employees)
    for department, employees in grouped_employees.items():
        print(f"Top 3 employees in {department}:")
        for employee in employees[:3]:
            print(f"{employee.name} - {employee.department} - {employee.salary}")

if __name__ == "__main__":
    main()
```