from itertools import groupby
from functools import cmp_to_key

def puzzle(states):
    statePairs = []
    sortedStates = sorted(states)
    uniqueStates = list(set(sortedStates))
    for a in uniqueStates:
        for b in uniqueStates:
            if a != b:
                statePairs.append((pkey(a + b), (a, b)))
    groupedPairs = [list(group) for key, group in groupby(sorted(statePairs, key=lambda x: x[0]), lambda x: x[0])]
    validPairs = list(filter(lambda x: len(x) > 1, groupedPairs))
    result = []
    for group in validPairs:
        for pair in group:
            if isValid(pair):
                result.append(pair)
    return result

def pkey(s):
    return ''.join(sorted(filter(str.isalpha, s.lower())))

def isValid(pair):
    (a0, a1) = pair[0]
    (b0, b1) = pair[1]
    return a0 != b0 and a0 != b1 and a1 != b0 and a1 != b1

def pairs(lst):
    result = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            result.append((lst[i], lst[j]))
    return result

states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
    "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

fakeStates = ["New Kory", "Wen Kory", "York New", "Kory New", "New Kory"]

puzzle(states + fakeStates)