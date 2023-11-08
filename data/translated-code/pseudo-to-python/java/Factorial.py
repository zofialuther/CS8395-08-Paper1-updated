from java.math import BigInteger
from java.util import InputMismatchException, Scanner

class IterativeFactorial:
    def factorial(self, n):
        if n is None:
            raise IllegalArgumentException
        elif n.signum() == -1:
            raise IllegalArgumentException("Argument must be a non-negative integer")
        else:
            factorial = 1
            for i in range(1, n+1):
                factorial = factorial * i
            return factorial

    def main(self, args):
        scanner = Scanner(System.in)
        number = BigInteger()
        result = BigInteger()
        error = False
        print("FACTORIAL OF A NUMBER")
        while True:
            print("Enter a number:")
            try:
                number = scanner.nextBigInteger()
                result = IterativeFactorial().factorial(number)
                error = False
                print("Factorial of " + str(number) + ": " + str(result))
            except InputMismatchException:
                error = True
                scanner.nextLine()
            except IllegalArgumentException:
                error = True
                scanner.nextLine()
            if not error:
                break
        scanner.close()