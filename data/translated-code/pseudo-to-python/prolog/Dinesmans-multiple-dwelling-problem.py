from itertools import permutations
from abs import abs

def rule1(L, Top):
    baker = [F for (person, F) in L if person == "baker"]
    return baker != Top

def rule2(L, Bottom):
    cooper = [F for (person, F) in L if person == "cooper"]
    return cooper != Bottom

def rule3(L, Top, Bottom):
    fletcher = [F for (person, F) in L if person == "fletcher"]
    return fletcher != Top and fletcher != Bottom

def rule4(L):
    miller = [Fm for (person, Fm) in L if person == "miller"]
    cooper = [Fc for (person, Fc) in L if person == "cooper"]
    return miller > cooper

def rule5(L):
    smith = [Fs for (person, Fs) in L if person == "smith"]
    fletcher = [Ff for (person, Ff) in L if person == "fletcher"]
    return abs(smith - fletcher) > 1

def rule6(L):
    cooper = [Fc for (person, Fc) in L if person == "cooper"]
    fletcher = [Ff for (person, Ff) in L if person == "fletcher"]
    return abs(cooper - fletcher) > 1

def init(L):
    Top = len(L)
    bottom = 1
    bagof = [F for (person, F) in L]
    LF = list(permutations(bagof))
    rule1(L, Top)
    rule2(L, bottom)
    rule3(L, Top, bottom)
    rule4(L)
    rule5(L)
    rule6(L)

def solve(L):
    bagof = [F for (person, F) in L]
    LF = list(permutations(bagof))
    label(LF)

def dinners():
    top = None
    bottom = None
    L = [('baker', None), ('cooper', None), ('fletcher', None), ('miller', None), ('smith', None)]
    init(L)
    solve(L)
    for item in L:
        print(item)