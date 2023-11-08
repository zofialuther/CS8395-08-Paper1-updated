```python
class EgyptianDivision:

    def __init__(self):
        pass

    @staticmethod
    def main():
        EgyptianDivision.divide(580, 34)

    @staticmethod
    def divide(dividend, divisor):
        powers_of_2 = []
        doublings = []

        line = 0
        while (2 ** line) * divisor <= dividend:
            power_of_2 = 2 ** line
            powers_of_2.append(power_of_2)
            doublings.append(power_of_2 * divisor)
            line += 1

        answer = 0
        accumulator = 0

        for i in range(len(powers_of_2) - 1, -1, -1):
            if accumulator + doublings[i] <= dividend:
                accumulator += doublings[i]
                answer += powers_of_2[i]

        print(f"{answer}, remainder {dividend - accumulator}")


EgyptianDivision.main()
```