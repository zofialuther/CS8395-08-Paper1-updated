def fizzbuzz():
    for x in range(1, 101):
        print_item(x)
        
def print_item(x):
    if x % 15 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
    print()