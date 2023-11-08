def congruence(Congruence, In, Fun, Out):
    In1 = list(map(lambda X: X % Congruence, In))
    Out1 = Fun(In1)
    Out = list(map(lambda X: X % Congruence, Out1))

def fun_1(X):
    return X ** 100 + X + 1

def fun_2(L):
    return sum(L)