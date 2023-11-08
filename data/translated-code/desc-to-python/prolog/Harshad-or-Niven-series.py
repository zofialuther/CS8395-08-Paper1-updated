from pyswip import Prolog

prolog = Prolog()
prolog.consult("lambda.pl")

list(prolog.query("niven(20, 1000)"))