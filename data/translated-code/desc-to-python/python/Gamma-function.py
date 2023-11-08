```python
import math

def gamma_function(x):
    # Precomputed values for the gamma function
    gamma_table = {1: 1, 2: 1, 3: 2, 4: 6, 5: 24, 6: 120}
    
    if x in gamma_table:
        return gamma_table[x]
    else:
        return (x - 1) * gamma_function(x - 1)

def main():
    for i in range(1, 10):
        print(f"Gamma({i}) = {gamma_function(i)}")

def format_output(value):
    return f"The gamma function of {value} is {gamma_function(value)}"

def enumerate_integers(start, end):
    for i in range(start, end):
        print(format_output(i))

if __name__ == "__main__":
    main()
```
