```python
import math

def main():
    for n in range(2, 6):
        unity(n)

def unity(n):
    print("\n", n, ":")
    for angle in range(0, int(2 * math.pi), int((2 * math.pi) / n)):
        real = math.cos(angle)
        if abs(real) < 1.0E-3:
            real = 0.0
        imag = math.sin(angle)
        if abs(imag) < 1.0E-3:
            imag = 0.0
        print("formatted coordinates", (real, imag))
```