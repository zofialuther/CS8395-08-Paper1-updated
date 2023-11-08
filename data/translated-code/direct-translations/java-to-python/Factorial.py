from typing import Any
import math

class IterativeFactorial:
    def factorial(self, n: Any) -> int:
        if n is None:
            raise ValueError
        elif n < 0:
            raise ValueError("Argument must be a non-negative integer")
        else:
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i
            return factorial

if __name__ == "__main__":
    number = None
    result = None
    error = False
    print("FACTORIAL OF A NUMBER")
    while not error:
        try:
            number = int(input("Enter a number: "))
            result = IterativeFactorial().factorial(number)
            error = False
            print(f"Factorial of {number}: {result}")
        except ValueError:
            error = True
            print("Invalid input. Please enter a non-negative integer.")
        except Exception as e:
            error = True
            print(f"An error occurred: {e}")
    input("Press Enter to exit")