```python
class Mod:
    def __init__(self, value, modulus):
        self.value = value % modulus
        self.modulus = modulus
    
    def __add__(self, other):
        if isinstance(other, Mod):
            return Mod(self.value + other.value, self.modulus)
        else:
            return Mod(self.value + other, self.modulus)
    
    def __sub__(self, other):
        if isinstance(other, Mod):
            return Mod(self.value - other.value, self.modulus)
        else:
            return Mod(self.value - other, self.modulus)
    
    def __mul__(self, other):
        if isinstance(other, Mod):
            return Mod(self.value * other.value, self.modulus)
        else:
            return Mod(self.value * other, self.modulus)
    
    def __eq__(self, other):
        if isinstance(other, Mod):
            return self.value == other.value and self.modulus == other.modulus
        else:
            return self.value == other
    
    def __str__(self):
        return str(self.value)
    
    def f(self, x):
        return Mod((self.value + x) * 2, self.modulus)

# Example usage
m = Mod(5, 12)
result = m.f(3)
print(result)
```