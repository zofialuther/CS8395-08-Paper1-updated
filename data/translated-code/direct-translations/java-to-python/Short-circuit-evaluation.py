```python
class ShortCirc:
    def main(self):
        print("F and F = ", self.a(False) and self.b(False), "\n")
        print("F or F = ", self.a(False) or self.b(False), "\n")

        print("F and T = ", self.a(False) and self.b(True), "\n")
        print("F or T = ", self.a(False) or self.b(True), "\n")

        print("T and F = ", self.a(True) and self.b(False), "\n")
        print("T or F = ", self.a(True) or self.b(False), "\n")

        print("T and T = ", self.a(True) and self.b(True), "\n")
        print("T or T = ", self.a(True) or self.b(True), "\n")

    def a(self, a):
        print("a")
        return a

    def b(self, b):
        print("b")
        return b

# Create an instance of the ShortCirc class and call the main method
s = ShortCirc()
s.main()
```