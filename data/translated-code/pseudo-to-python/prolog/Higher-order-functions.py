def first(Predicate):
    Predicate()

def second(Argument):
    print(Argument)

first(lambda: second('Hello World!'))