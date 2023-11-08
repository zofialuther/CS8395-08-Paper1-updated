from pyswip import Prolog, Functor, Variable, Query

def zebra():
    prolog = Prolog()
    prolog.consult("zebra.pl")

    for soln in prolog.query("zebra(Nation, Color, Smoke, Pet, Drink)"):
        print(soln["Nation"], soln["Color"], soln["Smoke"], soln["Pet"], soln["Drink"])

zebra()