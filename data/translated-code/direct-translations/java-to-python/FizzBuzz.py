def fizz_buzz():
    number = 1
    while number <= 100:
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
        number += 1

fizz_buzz()