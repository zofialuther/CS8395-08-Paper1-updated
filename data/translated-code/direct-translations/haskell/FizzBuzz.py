main = map(lambda x: print(x), list(map(lambda x, y: str(x) if y == '' else y, range(1, 101), fizz_buzz_list)))

fizz_buzz_list = list(map(lambda x, y: x + y, cycle(['', '', 'Fizz']), cycle(['', '', '', '', 'Buzz'])))