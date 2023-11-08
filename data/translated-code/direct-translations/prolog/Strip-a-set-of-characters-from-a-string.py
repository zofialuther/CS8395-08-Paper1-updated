from pyswip import Prolog, Functor, Variable, Query

prolog = Prolog()
prolog.consult("library(lambda)")

def stripchars(String, Exclude, Result):
    Result1 = list(filter(lambda x: x not in Exclude, String))
    Result = ''.join(Result1)
    return Result

# Example usage
print(stripchars("hello", ['l', 'o'], ""))