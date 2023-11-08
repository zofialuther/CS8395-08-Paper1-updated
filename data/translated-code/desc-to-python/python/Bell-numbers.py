```python
from functools import reduce

def bell_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [triangle[i-1][-1]]
        for j in range(i):
            row.append(row[-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle

def bell_number(n):
    return reduce(lambda x, y: x + y, bell_triangle(n)[-1])

def display_bell_numbers(n):
    for i in range(1, n+1):
        print(f"Bell number {i}: {bell_number(i)}")

def display_bell_triangle(n):
    triangle = bell_triangle(n)
    for row in triangle:
        print(row)

def main():
    display_bell_numbers(15)
    print(f"The fiftieth Bell number is: {bell_number(50)}")
    display_bell_triangle(10)

if __name__ == "__main__":
    main()
```