from pyswip import Prolog

prolog = Prolog()
prolog.consult("path_to_file.pl")

# Define congruence function
def congruence(Congruence, In, Fun, Out):
    In1 = list(map(lambda x: x % Congruence, In))
    Out1 = Fun(In1)
    Out = list(map(lambda x: x % Congruence, Out1))
    return Out

# Define fun_1
def fun_1(X):
    return [X[0]**100 + X[0] + 1]

# Define fun_2
def fun_2(L):
    return [sum(L)]

# Query the congruence function
result = list(congruence(5, [1, 2, 3], fun_1, [1, 2, 3]))
print(result)