from typing import ClassVar

class IntegerArithmetic:
    def main(self):
        from typing import ClassVar
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        sum = a + b
        difference = a - b
        product = a * b
        division = a // b
        remainder = a % b

        print("a + b = ", sum)
        print("a - b = ", difference)
        print("a * b = ", product)
        print("quotient of a / b = ", division)
        print("remainder of a / b = ", remainder)

obj = IntegerArithmetic()
obj.main()