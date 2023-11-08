from pyswip import Prolog

prolog = Prolog()
prolog.consult("niven.pl")

for soln in prolog.query("niven"):
    print(soln)