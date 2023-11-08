```python
class Farey:
    class Frac:
        def __init__(self, num, den):
            self.num = num
            self.den = den
            
        def value(self):
            return self.num / self.den
        
        def __lt__(self, other):
            return self.value() < other.value()

    @staticmethod
    def genFarey(denominator):
        farey_set = set()
        for i in range(denominator + 1):
            for j in range(i + 1, denominator + 1):
                farey_set.add(Farey.Frac(i, j))
        return sorted(farey_set, key=lambda x: x.value())

    @staticmethod
    def main():
        for d in range(1, 12):
            farey_sequence = Farey.genFarey(d)
            print(f"Farey sequence for denominator {d}: {farey_sequence}")
        
        for d in range(100, 1001, 100):
            farey_sequence = Farey.genFarey(d)
            print(f"Number of fractions in Farey sequence for denominator {d}: {len(farey_sequence)}")

Farey.main()
```