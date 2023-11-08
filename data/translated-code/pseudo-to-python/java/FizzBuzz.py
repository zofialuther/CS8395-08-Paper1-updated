number = 1
while number <= 100:
    print("FizzBuzz" if number % 15 == 0 else "Fizz" if number % 3 == 0 else "Buzz" if number % 5 == 0 else number)
    number += 1