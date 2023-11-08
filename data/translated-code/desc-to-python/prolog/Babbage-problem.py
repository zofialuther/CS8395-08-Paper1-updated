from pyswip import Prolog, Functor, Variable

prolog = Prolog()
prolog.consult("clpfd")

def babbage_3(N, Square, EndDigits):
    N #=< 10**((EndDigits + 3) // 6)
    Square #= N*N
    Square mod 1000000 #= EndDigits

def babbage():
    X = Variable()
    Y = Variable()
    Z = Variable()
    EndDigits = 269696
    babbage_3(X, Y, EndDigits)
    for soln in prolog.query(babbage_3(X, Y, EndDigits)):
        print("The lowest number is: ", soln[X])

babbage()