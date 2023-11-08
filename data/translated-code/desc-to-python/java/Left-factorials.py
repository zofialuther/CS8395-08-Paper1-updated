```python
import math

def left_factorial(n):
    result = 0
    for i in range(n+1):
        result += math.factorial(i)
    return result

def main():
    input_values = [5, 10, 15, 20]
    for value in input_values:
        factorial_result = left_factorial(value)
        print(f"Left factorial of {value}: {factorial_result}")
        print(f"Number of digits in result: {len(str(factorial_result))}")

if __name__ == "__main__":
    main()
```