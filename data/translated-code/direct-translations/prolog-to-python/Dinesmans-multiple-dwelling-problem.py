from itertools import permutations
from pyswip import Prolog, Functor, Variable

prolog = Prolog()

prolog.assertz("bottom(1)")
prolog.assertz("top(5)")

def solve():
    people = ["baker", "cooper", "fletcher", "miller", "smith"]
    floors = [1, 2, 3, 4, 5]

    # Define the rules
    def rule1(L):
        return L["baker"] != 5

    def rule2(L):
        return L["cooper"] != 1

    def rule3(L):
        return L["fletcher"] != 1 and L["fletcher"] != 5

    def rule4(L):
        return L["miller"] > L["cooper"]

    def rule5(L):
        return abs(L["smith"] - L["fletcher"]) > 1

    def rule6(L):
        return abs(L["fletcher"] - L["cooper"]) > 1

    for permutation in permutations(floors):
        L = {person: floor for person, floor in zip(people, permutation)}
        if all(rule(L) for rule in [rule1, rule2, rule3, rule4, rule5, rule6]):
            return L

solution = solve()
print(solution)