```python
class RN:
    class Numeral(Enum):
        I = 1
        IV = 4
        V = 5
        IX = 9
        X = 10
        XL = 40
        L = 50
        XC = 90
        C = 100
        CD = 400
        D = 500
        CM = 900
        M = 1000
    
    def roman(self, num):
        result = ""
        for value in reversed(list(self.Numeral)):
            while num >= value.value:
                result += value.name
                num -= value.value
        return result
    
    def test(self):
        print(self.roman(3)) # III
        print(self.roman(9)) # IX
        print(self.roman(58)) # LVIII
        print(self.roman(1994)) # MCMXCIV
    
    def main(self):
        self.test()
```