from constraint import *

# Basic, Q = Quarter, D = Dime, N = Nickel, P = Penny
def coins(Q, D, N, P, T):
    problem = Problem()
    problem.addVariable('Q', range(T+1))
    problem.addVariable('D', range(T+1))
    problem.addVariable('N', range(T+1))
    problem.addVariable('P', range(T+1))
    problem.addConstraint(lambda q, d, n, p: (q * 25) + (d * 10) + (n * 5) + p == T, ('Q', 'D', 'N', 'P'))
    solutions = problem.getSolutions()
    return solutions

def coins_for(T):
    return coins('Q', 'D', 'N', 'P', T)