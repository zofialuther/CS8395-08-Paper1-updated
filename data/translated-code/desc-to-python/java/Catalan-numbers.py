```python
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def catalan_factorial(n):
    return factorial(2*n) // (factorial(n+1) * factorial(n))

def catalan_recursive(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_recursive(i) * catalan_recursive(n-i-1)
    return res

def catalan_math(n):
    return factorial(2*n) // (factorial(n+1) * factorial(n))

def main():
    for i in range(15):
        print(f"Catalan number {i+1} using factorial formula: {catalan_factorial(i)}")
        print(f"Catalan number {i+1} using recursive formula: {catalan_recursive(i)}")
        print(f"Catalan number {i+1} using mathematical formula: {catalan_math(i)}")

if __name__ == "__main__":
    main()
```