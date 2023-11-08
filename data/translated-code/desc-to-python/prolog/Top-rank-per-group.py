```python
def topDeps(department_data, N):
    for department in department_data:
        top_employees = findTopEmployees(department_data[department], N)
        print(f"Department: {department}")
        for employee in top_employees:
            print(f"ID: {employee['id']}, Name: {employee['name']}, Salary: {employee['salary']}")

def findTopEmployees(employees, N):
    if N == 0 or len(employees) == 0:
        return []
    else:
        top_employee = max(employees, key=lambda x: x['salary'])
        remaining_employees = [emp for emp in employees if emp != top_employee]
        return [top_employee] + findTopEmployees(remaining_employees, N-1)

# Example usage
department_data = {
    "HR": [
        {"id": 1, "name": "John", "salary": 50000},
        {"id": 2, "name": "Alice", "salary": 55000},
        {"id": 3, "name": "Bob", "salary": 52000}
    ],
    "IT": [
        {"id": 4, "name": "Emily", "salary": 60000},
        {"id": 5, "name": "David", "salary": 58000},
        {"id": 6, "name": "Sarah", "salary": 61000}
    ]
}

topDeps(department_data, 2)
```