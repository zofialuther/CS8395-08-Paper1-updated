def first(predicate):
    return predicate()

def second(argument):
    print(argument)

first(second('Hello World!'))