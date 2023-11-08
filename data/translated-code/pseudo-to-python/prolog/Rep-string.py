def test_for_repstring(String, Result, Reps):
    if set(repstring(String, Rep) for Rep in Reps):
        Result = 'no repstring'
    else:
        Result = 'repstrings'
        Reps = []

def repstring(Codes, R):
    RepLength = random.randint(1, len(Codes))
    R = [0] * RepLength
    phrase(rep(R), prefix(Codes, R))

def rep(X):
    return X, X

def report_repstring(S, Result, Reps):
    print(S, Result)
    for R in Reps:
        print(R)

def report_repstrings():
    Results = maplist(test_for_repstring, test_strings)
    maplist(report_repstring, Results)