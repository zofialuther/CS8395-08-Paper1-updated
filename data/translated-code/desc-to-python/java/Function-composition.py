```python
import math

class Compose:
    def __init__(self):
        pass
    
    @staticmethod
    def compose(f, g):
        return lambda x: f(g(x))

def main():
    composed_function = Compose.compose(math.sin, math.asin)
    result = composed_function(0.5)
    print(result)

if __name__ == "__main__":
    main()
```