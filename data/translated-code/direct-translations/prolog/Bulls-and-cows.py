from random import randint

from pyswip import Functor, Variable, Query, call

proposition = Functor("proposition", 1)
digits = Functor("digits", 1)
study = Functor("study", 4)

call('use_module', 'library(lambda)')
call('use_module', 'library(clpfd)')

# Parameters of the server
proposition(4)
digits(8)


def bulls_and_cows_server():
    len_guess = Variable()
    solution = Variable()
    choose = Functor("choose", 1)

    call('length', solution, len_guess)
    call(choose, solution)

    while True:
        guess = input('Your guess : ')

        query = Query(study, solution, guess, Variable(), Variable())
        if query.nextSolution():
            Bulls = query.getBinding(Variable())
            Cows = query.getBinding(Variable())
            print('Bulls :', Bulls, 'Cows :', Cows)
            if Bulls == len_guess.value:
                break
        else:
            Digits = Variable()
            Max = Digits + 1
            print(f'Guess must be of {len_guess.value} digits between 1 and {Max}')
            break


def choose(solution):
    digits = Variable()
    Max = digits + 1

    while True:
        solution.value = [randint(1, Max) for _ in range(solution.value)]
        if len(set(solution.value)) == solution.value:
            break


def study(solution, guess, bulls, cows):
    len_guess = Variable()
    digits = Variable()

    chars = list(guess)
    ms = [int(x) for x in chars]

    if len(ms) != len_guess.value or any(x <= 0 or x > digits.value + 1 for x in ms):
        return False

    bulls.value = sum(x == y for x, y in zip(solution.value, ms))

    cows.value = sum(sum(x == y1 for x in ms) for y1 in solution.value) - bulls.value

    return True


bulls_and_cows_server()