```python
def fib_stream():
    last_fib = [0]
    def fib_generator():
        while True:
            if len(last_fib) == 1:
                last_fib.append(1)
            else:
                last_fib = [last_fib[-1], sum(last_fib)]
            yield last_fib[-1]
    return fib_generator()

def fib(n):
    return list(fib_stream())[n-1]

# Example usage:
print(fib(5))  # Output: 5
```